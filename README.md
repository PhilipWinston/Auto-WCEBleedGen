# Auto-WCEBleedGen Challenge 🔬🤖

A solution developed for the Auto-WCEBleedGen Challenge hosted by MISAHUB. The goal is to classify bleeding vs. non-bleeding endoscopy frames and detect the bleeding regions using deep learning and computer vision techniques.

## 🧑‍💻 Role
**Lead Developer**  
Developed and trained a robust model using **Python** and **YOLOv8** to address both classification and detection of bleeding in wireless capsule endoscopy images.

---

## 🗂️ Dataset
The training dataset includes:
- Endoscopy frames labeled as **bleeding** or **non-bleeding**
- Medically validated **binary masks** and **bounding boxes** in `.txt`, `.xml`, and YOLO format

📁 Dataset access: [Training Dataset - Official Link](https://misahub.in/CVIP/challenge.html)

### 📊 Dataset Split
- 80% for Training
- 20% for Validation

---

## 🧠 Model Architecture
- **Classification:** Binary classifier using YOLOv8 backbone
- **Detection:** Object detection to localize bleeding regions
- **Interpretability:** Class Activation Maps (CAMs) included

---

## 📈 Evaluation Metrics


#Classification:
![confusion_matrix](https://github.com/PhilipWinston/Auto-WCEBleedGen/assets/145428055/969c45a2-9f62-4fb2-ac7c-bb02d36bc9cc)
![results](https://github.com/PhilipWinston/Auto-WCEBleedGen/assets/145428055/de90ea34-8e0e-48db-bf00-f788459405e4)
#Accuracy=0.99427
#Recall=1
#f1 score=0.994236

#Detection 
![F1_curve](https://github.com/PhilipWinston/Auto-WCEBleedGen/assets/145428055/c6f7b4ef-66cb-43f2-99a0-bbe53a327ccb)
![PR_curve](https://github.com/PhilipWinston/Auto-WCEBleedGen/assets/145428055/202adf6a-220a-471c-84c7-cc7ff9923322)
![results](https://github.com/PhilipWinston/Auto-WCEBleedGen/assets/145428055/3a2a3be5-5b81-42e4-8936-bba68dfc15f1)
![R_curve](https://github.com/PhilipWinston/Auto-WCEBleedGen/assets/145428055/302dae7e-9e53-4235-90cb-a56eafa14768)
![P_curve](https://github.com/PhilipWinston/Auto-WCEBleedGen/assets/145428055/234bf677-d4df-4fa8-8b1e-821ae65df89c)

#2.
![val_batch0_labels](https://github.com/PhilipWinston/Auto-WCEBleedGen/assets/145428055/2bdb8fa6-6128-46ba-ae0a-b5dd5a0655da)
![val_batch0_labels](https://github.com/PhilipWinston/Auto-WCEBleedGen/assets/145428055/d94204e0-7222-4294-8b09-fc93961e2a5e)

#4.
![Screenshot 2023-10-09 205421](https://github.com/PhilipWinston/Auto-WCEBleedGen/assets/145428055/a656b89b-d6fe-44ea-8ccd-c0398af807cc)
![Screenshot 2023-10-09 205713](https://github.com/PhilipWinston/Auto-WCEBleedGen/assets/145428055/7223074d-256d-45f9-8c71-f119a01c150b)





