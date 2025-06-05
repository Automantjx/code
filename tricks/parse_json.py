import json
# dump  --  由python对象格式化为json字符串

person = {
    "name" : "xixi",
    "age" : 20,
    "favoriate" : "xingxing",
    "tel" : [10, 20],
    "beaty" : True
}

json_str = json.dumps(person, indent=4, sort_keys=True) # indent-缩进  sort_keys-键排序
print(person, type(person))  # 字典 单引号
print(json_str, type(json_str)) # 字符串 双引号


#####
json.dump(person, open('data.json','w'), indent=4)  


# load  --  使用json字符串生成python对象
python_obj = json.loads(json_str)
print(python_obj)

#####
with open('data.json', 'r') as f:
    content = json.load(f)
    print(content)

print(content["tel"])

import pandas as pd
df = pd.DataFrame(content["tel"])
print(df)
df1 = df.iloc[:1,:]
print(df1)





# 封装一下
import json

def read_json(filename):
    """
    读取JSON文件并返回数据。

    :param filename: JSON文件的路径
    :return: 从JSON文件中读取的数据
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"文件 {filename} 未找到.")
        return None
    except json.JSONDecodeError:
        print(f"文件 {filename} 不是有效的JSON.")
        return None

def write_json(data, filename):
    """
    将数据写入JSON文件。

    :param data: 要写入文件的数据
    :param filename: JSON文件的路径
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"数据已成功写入 {filename}.")
    except TypeError:
        print("提供的数据无法序列化为JSON.")
    except IOError:
        print(f"写入文件 {filename} 时出错.")

# 示例使用
if __name__ == "__main__":
    # 示例数据
    sample_data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # 写入数据到JSON文件
    write_json(sample_data, 'sample.json')

    # 从JSON文件读取数据
    read_data = read_json('sample.json')
    print(read_data)
