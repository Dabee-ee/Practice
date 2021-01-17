def save_to_file(img):
  n = 1
  for i in img:
    imgurl = i["src"]
    with urlopen(imgurl) as f:
      with open("mario" + str(n) + '.gif', 'wb') as h:
        img = f.read()
        h.write(img)
  n += 1  