#Making Faces
def main():
    userinput = input("")
    print(convert(userinput))

def convert(emoticon):
    emoticon = emoticon.replace(":)","🙂")
    emoticon = emoticon.replace(":(","🙁")
    return emoticon


main()
