# 🩸 AnemiaSense - Detect Anemia using Machine Learning  

AnemiaSense is a simple and powerful **Streamlit web app** that predicts whether a person is **anemic or not** using **machine learning models** based on blood test parameters.

---

## 🌐 Live Demo  
🔗 **Try it here:** [AnemiaSense Streamlit App](https://anemia-sense-7sv2zgssyo5hmysgl9p7sg.streamlit.app/)  

---

## 🚀 Features  
- 🧬 Predicts anemia using input parameters:  
  - Hemoglobin (g/dL)  
  - MCH (Mean Corpuscular Hemoglobin)  
  - MCHC (Mean Corpuscular Hemoglobin Concentration)  
  - MCV (Mean Corpuscular Volume)  
  - Gender  
- 💻 Easy-to-use and interactive **Streamlit interface**  
- 🤖 Model built using **Random Forest Classifier**  
- ⚡ Provides **instant predictions**  
- 🩺 Promotes health awareness using **AI in healthcare**  

---

## 🧠 Tech Stack  
- 🐍 **Python** – Programming Language  
- 💻 **Streamlit** – Web App Framework  
- 🤖 **Scikit-learn** – Machine Learning Library  
- 🧾 **Pandas** – Data Analysis and Preprocessing  
- 💾 **Joblib** – Model Saving and Loading  

---

## ⚙️ How to Run Locally  

Follow these steps to run the app on your system 👇  

```bash
# 1️⃣ Clone this repository
git clone https://github.com/Sankeerthika/anemia-sense.git

# 2️⃣ Navigate to the project folder
cd anemia-sense

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the Streamlit app
streamlit run week3_anemiasense_app_py.py



## 🧬 Input Example
| Gender | Hemoglobin | MCH | MCHC | MCV |
|:-------|:-----------:|:---:|:----:|:---:|
| Female | 10.5 | 25 | 30 | 75 |

➡️ Output: **🔴 The person is Anemic. Please consult a healthcare professional.**


📂 Project Structure
anemia-sense/
├── .devcontainer/                 # Optional container setup (for VS Code)
├── model.pkl                      # Trained ML model file
├── requirements.txt               # Dependencies
├── week3_anemiasense_app_py.py    # Main Streamlit app
├── README.md                      # Documentation file


🩺 What is Anemia?

Anemia is a medical condition in which the blood doesn’t have enough healthy red blood cells to carry oxygen to your body’s tissues.
It can make you feel tired, weak, or short of breath.
Common causes include iron deficiency, vitamin deficiency, or chronic diseases.

AnemiaSense helps you get a quick idea of whether you might have anemia — but it’s not a medical diagnosis tool. Always consult a healthcare professional for medical advice.


 Current Features (Already Implemented)

📊 Bar chart comparing user’s Hemoglobin, MCH, MCHC, MCV with normal ranges

🔥 Severity levels: Normal, Mild, Moderate, Severe

🍎 Diet recommendations to improve hemoglobin

✅ Instant prediction based on trained ML model

 Future Enhancements

📱 Fully mobile responsive UI

🚀 More blood indicators (RBC count, PCV, Iron levels)

☁ Save user history in database

🤖 Train model on larger anemia dataset for higher accuracy

🧪 Add more types of anemia classifications
## 🏆 Author
**Sankeerthika Paka**  
B.Tech CSE Student, Anurag University  

Empowering Health with AI

🪙 License

This project is licensed under the MIT License — feel free to use, modify, and share it for learning purposes.





