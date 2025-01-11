import pygame as p
import subprocess
import time


us_image_list = []
image_name_list = subprocess.run(["ls","./images/"], stdout=subprocess.PIPE)
image_name_list = str(image_name_list.stdout, encoding="UTF-8").split("\n")
image_name_list.pop(-1)
print(image_name_list)

for element in image_name_list:
    us_image_list.append(p.image.load("./images/" + element))

main_size = us_image_list[0].get_size()
image_list = []
for element in us_image_list:
    image_list.append(p.transform.scale(element, main_size))
merged_image = p.surface.Surface(main_size)
print(image_list[0].get_at((0,0)))
image_count = len(image_list)
window = p.display.set_mode(main_size)

for x in range(main_size[0]):
    window.blit(merged_image,(0,0))
    p.display.flip()
    for y in range(main_size[1]):
        r, g, b = (0, 0, 0)
        for n in range(image_count):
            rgba = image_list[n].get_at((x,y))
            r += rgba[0]
            g += rgba[1]
            b += rgba[2]
        merged_image.set_at((x,y),(int(r / image_count), int(g / image_count), int(b / image_count)))
p.image.save(merged_image, str(time.time()) + ".png")
p.quit()