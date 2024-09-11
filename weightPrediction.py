import streamlit as st

class WeightPrediction:

    def __init__(self):
        # Initialize variables in session_state for persistence
        if 'name' not in st.session_state:
            st.session_state.name = ""
        if 'age' not in st.session_state:
            st.session_state.age = 23
        if 'height' not in st.session_state:
            st.session_state.height = 150
        if 'gender' not in st.session_state:
            st.session_state.gender = ""
        if 'weight_kg' not in st.session_state:
            st.session_state.weight_kg = ""
        if 'actual_weight' not in st.session_state:
            st.session_state.actual_weight = ""

    def input_data(self):

        try:
            st.title("Welcome to Weight and Beauty Prediction")

            st.warning("Try at your Own Risk ⚠️")

            st.sidebar.title("Provide Your Personal Details!!!")

            # Use session_state to store user input
            st.session_state.name = st.sidebar.text_input("Enter Your Name : ", st.session_state.name).lower()

            st.session_state.age = st.sidebar.slider("Select your age:", 0, 60, st.session_state.age)

            st.sidebar.info("If your age is over 60: You are alive, that’s important. Bless you, you will die soon. 🙏")

            st.session_state.height = st.sidebar.slider("Select your height in cm:", 0, 200, st.session_state.height)

            st.session_state.gender = st.sidebar.radio("Select your gender:", ("Male", "Female"), index=0 if st.session_state.gender == "Male" else 1)

            st.sidebar.error("If you have 🍆 and 🍒 both, this app is not for you.")

            if st.button("Predict Expected Weight"):

                st.session_state.weight_kg = self.weight_logic()

            # Display the predicted weight if available
            if st.session_state.weight_kg != None and st.session_state.weight_kg != "":

                st.success(f"{st.session_state.name} your Predicted BMI Weight is {st.session_state.weight_kg:.2f}")

                st.session_state.actual_weight = st.text_input("Enter Your Current Weight :", st.session_state.actual_weight)

                # Handle beauty prediction
                if st.button("Predict Your Beauty"):

                    if st.session_state.actual_weight == "":

                        st.error("Mother Fucker, type Your current Weight 🖕")

                    else:

                        if st.session_state.gender == "Male":

                            if (int(st.session_state.weight_kg) - 5) <= int(st.session_state.actual_weight) <= (int(st.session_state.weight_kg) + 5):

                                st.success("You think you are stud guy")

                                st.header("I'm fucking lion 🦁")

                                st.image("depositphotos_74737809-stock-photo-man-with-open-shirt-flirts.jpg")

                                st.success("But according to AI your messages are ignored on insta 🤣")

                                st.image("34e1b45cfe98e66876959587c458d458.jpg")

                            elif (int(st.session_state.weight_kg) - 5) >= int(st.session_state.actual_weight):

                                st.error("You think you are fit and fine")

                                st.header("my shadow has abs")

                                st.image("stock-photo-thin-guy-poses-on-workout-in-gym-dystrophic-1239438094.jpg")

                                st.error("But according to AI You Are muthal ✊")

                                st.header("Regrets")

                                st.image("istockphoto-522171599-612x612.jpg")

                            elif (int(st.session_state.weight_kg) + 5) <= int(st.session_state.actual_weight):

                                st.error("You think you are cute kalu")

                                st.header("I have big 🍒 then girls")

                                st.image("images.jpeg")

                                st.error("But According to AI you are :")

                                st.header("😵‍💫")

                                st.image("images (1).jpeg")

                                st.image("funny-fat-guy-fitness-and-healthy-lifestyle-white-background-2F6CW8X.jpg")

                        elif st.session_state.gender == "Female":

                            if (int(st.session_state.weight_kg) - 5) <= int(st.session_state.actual_weight) <= (int(st.session_state.weight_kg) + 5):

                                st.success("AI predict you as beauty queen but at the end you fall for Red Flag 🍎.")

                                st.header("I'm 💦 ohhh yeahhhhh")

                                st.image("portrait-of-a-man-in-a-bright-red-curly-wig-funny-facial-expressions-on-the-background-photo.jpeg")

                            elif (int(st.session_state.weight_kg) - 5) >= int(st.session_state.actual_weight):

                                st.error("You think you are")

                                st.header("Fitness chases me")

                                st.image("beautiful-deer-green-meadow_315346-11.jpg")

                                st.error("But According to AI you are :")

                                st.header("Skinny with No 🍒 and 🍑")

                                st.image("so-skinny.jpeg")

                            elif (int(st.session_state.weight_kg) + 5) <= int(st.session_state.actual_weight):

                                st.error("You think you are chubby girl ")

                                st.header("Cute Motu")

                                st.image("istockphoto-184987985-612x612.jpg")

                                st.error("but according to AI you are :")

                                st.header("GENDA")

                                st.image("istockphoto-139960934-612x612.jpg")

        except Exception as exception:

            st.write(exception)

    def weight_logic(self):

        try:
            if st.session_state.name == "":

                st.error("Enter Your Fucking Name 😡")

                return None

            else:

                target_bmi = 0

                height_m = st.session_state.height / 100.0

                if st.session_state.gender.lower() == 'male':

                    target_bmi = 24

                    if st.session_state.age < 18:

                        target_bmi -= 1

                    elif st.session_state.age > 50:

                        target_bmi += 1

                elif st.session_state.gender.lower() == 'female':

                    target_bmi = 22

                    if st.session_state.age < 18:

                        target_bmi -= 1

                    elif st.session_state.age > 50:

                        target_bmi += 1

                weight_kg = target_bmi * (height_m ** 2)

                return weight_kg

        except Exception as exception:

            st.write(exception)


weightPrediction = WeightPrediction()
weightPrediction.input_data()
