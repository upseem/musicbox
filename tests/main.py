# 分离音频和人声
from audio_separator.separator import Separator
import os

def get_all_mp3_files(directory):
    mp3_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp3'):
                mp3_files.append(os.path.join(root, file))
    return mp3_files


mdoel_path = "./model"
# 初始化 Separator 类（带有可选的配置属性，见下文）
separator = Separator()

separator.model_file_dir = mdoel_path

# 加载机器学习模型（如果未指定，默认为 'model_mel_band_roformer_ep_3005_sdr_11.4360.ckpt'）
separator.load_model(model_filename="UVR-MDX-NET_Main_438.onnx")
# separator.load_model(model_filename="UVR-MDX-NET-Inst_full_292.onnx")

separator.output_format = "WAV"
separator.output_dir = "./out"


# 对特定音频文件进行分离而不重新加载模型
# output_files = separator.separate('./mp3/c.mp3')

mp3_directory = './mp3'
mp3_files = get_all_mp3_files(mp3_directory)
for mp3_file in mp3_files:
        print(f"Processing file: {mp3_file}")
        output_files = separator.separate(mp3_file)
        # 处理 output_files 或执行其他操作
  
for mp3_file in mp3_files:
        try:
            print(f"Processing file: {mp3_file}")
            output_files = separator.separate(mp3_file)
            # 处理 output_files 或执行其他操作
        except Exception as e:
            print(f"Failed to process file {mp3_file}: {e}") 
            continue     
print(f"分离完成！输出文件：{' '.join(output_files)}")
