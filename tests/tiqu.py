import json
from NEMbox.api import NetEase

def save_to_txt(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(f"{item['id']} {item['name']}\n")

def extract_id_name(data):
    extracted_data = []
    seen_ids = set()
    
    for item in data:
        song_id = item.get('id')
        song_name = item.get('name')
        if song_id and song_name and song_id not in seen_ids:
            extracted_data.append({
                'id': song_id,
                'name': song_name
            })
            seen_ids.add(song_id)
    
    return extracted_data

def main():
    api = NetEase()
    artist_id = 6731
    
    print("Fetching artist data...")
    artist_data = api.artists(artist_id)
    print("Artist data fetched:", artist_data)
    
    if artist_data:
        extracted_data = extract_id_name(artist_data)
        save_to_txt(extracted_data, 'a.txt')
        print("Extracted data saved to a.txt")
    else:
        print("Failed to fetch artist data.")

if __name__ == "__main__":
    main()
