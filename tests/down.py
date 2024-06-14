import requests

def read_ids_and_names(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    id_name_pairs = []
    for line in lines:
        line = line.strip()
        if line:
            song_id, name = line.split(' ', 1)
            id_name_pairs.append((song_id, name))
    
    return id_name_pairs

def download_mp3(song_id, name):
    url = f"http://music.163.com/song/media/outer/url?id={song_id}.mp3"
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        with open(f"./mp3/{name}.mp3", 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f"Downloaded: {name}.mp3")
    else:
        print(f"Failed to download: {name}.mp3")

def main():
    id_name_pairs = read_ids_and_names('a.txt')
    for song_id, name in id_name_pairs:
        download_mp3(song_id, name)

if __name__ == "__main__":
    main()
