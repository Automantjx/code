import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt

demo_tree = ET.parse("_uw_engine_runtime.xosc")
demo_root = demo_tree.getroot()
vertexs = (
    demo_root.find("Storyboard")
    .find("Story")
    .find("Act")
    .find("ManeuverGroup")
    .find("Maneuver")
    .find("Event")
    .find("Action")
    .find("PrivateAction")
    .find("RoutingAction")
    .find("FollowTrajectoryAction")
    .find("Trajectory")
    .find("Shape")
    .find("Polyline")
    .findall("Vertex")
)

times, positions = [], []
for vertex in vertexs:
    times.append(vertex.attrib)
    positions.append(vertex.find("Position").find("WorldPosition").attrib)
x_coords = [float(position["x"]) for position in positions]
y_coords = [float(position["y"]) for position in positions]
times = [float(time["time"]) for time in times]
# plt.plot(times, x_coords)
plt.plot(x_coords, y_coords)

# def generate_trajectory(original_trajectory, accel_duration, decel_duration):           
#     total_distance = original_trajectory[-1] - original_trajectory[0]  
#     max_velocity = total_distance / (accel_duration + decel_duration) 
    
#     n = len(original_trajectory)  
#     velocities = np.zeros(n)  
#     positions = np.zeros(n)  
      
#     for i in range(accel_duration):  
#         velocities[i] = i * max_velocity / accel_duration  
#         positions[i] = np.sum(velocities[:i+1]) * (original_trajectory[1] - original_trajectory[0]) / max_velocity  
            
#     for i in range(accel_duration, n):  
#         velocities[i] = max_velocity - (i - accel_duration + 1) * max_velocity / decel_duration  
#         positions[i] = positions[i-1] + velocities[i] * (original_trajectory[1] - original_trajectory[0])  
       
#     scale_factor = total_distance / (positions[-1]+np.finfo(float).eps)  
#     positions *= scale_factor    
      
#     return positions 

  
def generate_trajectory(original_trajectory, accel_duration, decel_duration):  
    n = len(original_trajectory)  
    total_distance = original_trajectory[-1] - original_trajectory[0]  
    max_velocity_reached = total_distance / (accel_duration + decel_duration)  
        
    uniform_duration = max(0, n - accel_duration - decel_duration)  
      
    # 初始化速度和位置数组  
    velocities = np.zeros(n)  
    positions = np.zeros(n)  
      
    # 加速阶段  
    for i in range(accel_duration):  
        velocities[i] = i * max_velocity_reached / accel_duration  
        positions[i] = positions[i-1] + velocities[i] 
      
    # 匀速阶段（如果有）  
    velocity_for_uniform = max_velocity_reached  
    for i in range(accel_duration, accel_duration + uniform_duration):  
        velocities[i] = velocity_for_uniform  
        positions[i] = positions[i-1] + velocity_for_uniform  
      
    # 减速阶段  
    for i in range(accel_duration + uniform_duration, n):  
        velocities[i] = max_velocity_reached - (i - accel_duration - uniform_duration + 1) * max_velocity_reached / decel_duration  
        positions[i] = positions[i-1] + velocities[i]  
      
    # 缩放位置数组以匹配总距离  
    scale_factor = total_distance / positions[-1]  
    positions *= scale_factor  
      
    return positions  


new_trajectory_x1 = generate_trajectory(x_coords[:20], 10, 10) + x_coords[0] # 0-2
new_trajectory_x2 = [new_trajectory_x1[-1] for _ in range(30)] # 2-5
new_trajectory_x3 = generate_trajectory(x_coords[20:31], 10, 0) + new_trajectory_x2[0]# 5-6
new_trajectory_x4 = np.linspace(new_trajectory_x3[-1], x_coords[-1], int((times[-1]-times[60])/0.1)) # 6-end
new_trajectory_x = [*new_trajectory_x1, *new_trajectory_x2, *new_trajectory_x3, *new_trajectory_x4]

new_trajectory_y1 = generate_trajectory(y_coords[:20], 10, 10) + y_coords[0]
new_trajectory_y2 = [new_trajectory_y1[-1] for _ in range(30)] # 2-5
new_trajectory_y3 = generate_trajectory(y_coords[20:31], 10, 0) + new_trajectory_y2[0]# 5-6
new_trajectory_y4 = np.linspace(new_trajectory_y3[-1], y_coords[-1], int((times[-1]-times[60])/0.1)) # 6-end
new_trajectory_y = [*new_trajectory_y1, *new_trajectory_y2, *new_trajectory_y3, *new_trajectory_y4]

plt.plot(new_trajectory_x, new_trajectory_y)

for i,vertex in enumerate(vertexs):
    world_position = vertex.find("Position").find("WorldPosition")
    world_position.attrib["x"] = str(new_trajectory_x[i])
    world_position.attrib["y"] = str(new_trajectory_y[i])

demo_tree.write("new_trajectory.xosc")

