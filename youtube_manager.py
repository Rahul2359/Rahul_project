import json
def load_data():
    try:
        with open('youtube.txt','r') as file:
            test=json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return[]
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print("\n")
    print("*" *70)
    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 70)

def add_video(videos):
    name=input('enter video name')
    time=input('enter video time:')
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input('enter the video number to update'))
    if 1 <= index <= len(videos):
        name=input('enter the new video name')
        time=input('enter the new video time')
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
    else:
        print('Invalid index selected')
def delete_video(videos):
    list_all_videos(videos)
    index=int(input('enter the video number to deleted'))
    if 1<=index>=len(videos):
        del videos[index-1]
        print('success')
        save_data_helper(videos)
    else:
        print('Invalid video index selected')
videos=load_data()
def main():
    while True:
        print('\n Youtube manager |choose an option')
        print('1.List all youtube videos')
        print('2.add a  youtube video')
        print('3.Update a youtube video details')
        print('4.Delete a youtube video')
        print('5.Exit the app')
        choice=input('enter your choice:')
        #print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case'5':
                break
            case _:
                print('invalid Choice')
if __name__=="__main__":
    main()