import face_recognition as fr
from PIL import Image, ImageDraw

student1 = fr.load_image_file("s1.png")
student2 = fr.load_image_file("s2.png")
student3 = fr.load_image_file("s3.png")
class_img = fr.load_image_file("class.png")

student1_encoding = fr.face_encodings(student1)[0]
student2_encoding = fr.face_encodings(student2)[0]
student3_encoding = fr.face_encodings(student3)[0]

locations = fr.face_locations(class_img)
class_encodings = fr.face_encodings(class_img)

print("Faces Detected :", len(locations))

if len(locations) == 0:
    print("No students detected")
    exit()

pil_image = Image.fromarray(class_img)
draw = ImageDraw.Draw(pil_image)

present = 0

student1_found = False
student2_found = False
student3_found = False

for location, encoding in zip(locations, class_encodings):

    if fr.compare_faces([student1_encoding], encoding)[0]:
        student1_found = True
        top, right, bottom, left = location
        draw.rectangle((left, top, right, bottom), outline="green", width=3)

    if fr.compare_faces([student2_encoding], encoding)[0]:
        student2_found = True
        top, right, bottom, left = location
        draw.rectangle((left, top, right, bottom), outline="green", width=3)

    if fr.compare_faces([student3_encoding], encoding)[0]:
        student3_found = True
        top, right, bottom, left = location
        draw.rectangle((left, top, right, bottom), outline="green", width=3)

print("\nAttendance Report")

if student1_found:
    print("dinkan- Present")
    present += 1
else:
    print("dinkan- Absent")

if student2_found:
    print("luttapi - Present")
    present += 1
else:
    print("luttapi - Absent")

if student3_found:
    print("thankan - Present")
    present += 1
else:
    print("thankan - Absent")

print("\nPresent :", present, "out of 3")

pil_image.save("attendance.png")
print("attendance.png saved")