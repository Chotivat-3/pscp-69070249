## บันทึกการแก้โจทย์
# 1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์: OJ2996 - [LEARNING LOGS] สลับตัวอักษร  
OJ submission ID: 541371  
สถานะ OJ: Pass  
เวลาที่ใช้คิดโจทย์และทำโจทย์ด้วยตนเอง: 0-15 minutes
# 2. ความเข้าใจโจทย์ของฉัน  
จากโจทย์ รับ input เข้ามาเป็น อักขระที่มีความยาว 5 ตัวอักษร และ output ส่งออกเป็น. 
เปลี่ยนลำดับการเรียงจากหลังไปหน้าแทน  
[abcde --> edcba]   
จากตอนแรกผมอ่านถึงเท่านี้และเริ่มทำ ทว่ายังผิดพลาดจากการอ่านโจทย์ไม่ครบ เนื่องจากโจทย์บอกว่า ควรเปลี่ยนเป็นตัวอักษรพิมพ์เล็ก!!!
# 3. วิธีแรก  
สร้างฟังชั่นก์ที่รับ input เข้ามาเเพื่อ กลับด้าน   
input ตัวอักษรภาษาอังกฤษ 5 ตัว  
ส่งข้อมูลเข้าฟังชั่นก์ เก็บค่าด้วยตัวแปร x  
จากนั้นเปลี่ยนตัวแปร x ให้กลับด้านต้วยการใช้ string slicing  
จากนั้นแสดงผลตัวแปร x เรียกใช้ฟังชั่น   
ทว่า output กลับด้านแล้วแต่ ตัวอักษรยังใหญ่เล็กตามเดิม
# 4. วิธีสุดท้ายที่เลือกใช้  
รับ input เข้ามาเป็นตัวอักษรอังกฤษ 5 ตัว ด้วยตัวแปร x  
จากนั้น เปลี่ยนตัวอักษรในตัวแปร x ให้เป็นตัวเล็กทั้งหมดและรับค่าตัวแปร x ตัวเล็กเเข้ามา ด้วย string method #x = x.lower()  
จากนั้น เอาตัวแปร x_ มารับ ข้อมูล x กลับด้าน  
ด้วยการใช้ string slicing #[::-]  
สุดท้ายส่ง output ด้วย #print(x_)
# 5. การทดสอบ  
test case 1 : กรณี ตัวอักษรตัวเล็กทั้งหมด   
input : abcde  
Expected output: : edcba  
Actual output: edcba  
Result: Pass  
test case 2 : กรณี ตัวอักษรตัวใหญ่ทั้งหมด   
input : ABCDE  
Expected output: : edcba  
Actual output: edcba  
Result: Pass  
test case 3 : กรณี ตัวอักษรสลับเล็กใหญ่  
input : AbCdE  
Expected output: : edcba  
Actual output: edcba  
Result: Pass 

# 6. การใช้ Ai : No
# 7. ความช่วยเหลือ ความร่วมมือ : No / ไม่มีใครช่วย / ไม่ได้คัดลอก Code

# 8. คำรับรองของนักศึกษา
Statement	Yes/No  
I wrote this submission in my own words.	Yes  
I understand my final code.	Yes  
I recorded the real OJ status.	Yes  
I did not copy AI-generated text directly into this file.	Yes  
I did not copy code from another person.	Yes  
If I received human help, I disclosed it in this file.	Yes  
I submitted the final code to the OJ by myself.	Yes
