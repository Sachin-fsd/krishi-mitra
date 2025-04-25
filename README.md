# 🌾 KrishiMitra - Smart Agricultural Yield Predictor

KrishiMitra is a lightweight, fully offline crop yield prediction tool designed for farmers in low-connectivity rural areas. It helps farmers make informed decisions about crop selection and resource management without requiring internet connectivity.

## Features

- 🌾 Offline crop yield prediction
- 📊 Input-based predictions using:
  - Soil type
  - Rainfall data
  - Temperature
  - Crop selection
  - Soil nutrients (Nitrogen, Phosphorus)
- 💡 Simple and intuitive user interface
- 📱 Works on basic laptops/desktops
- 🔊 Voice output for predictions
- 📈 Data visualization and analysis

## Installation

1. Ensure you have Python 3.8 or higher installed
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place your crop yield dataset (crop_yield_train.csv) in the project directory
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Launch the application using the command above
2. Navigate to "Predict Yield" in the sidebar
3. Enter the required parameters:
   - Select your crop type
   - Choose soil type
   - Input rainfall data
   - Enter temperature
   - Add soil nutrient information
4. Click "Predict Yield" to get the prediction
5. View the results and listen to the voice output

## Data Analysis

The application includes a data analysis section that provides:
- Basic statistics about the dataset
- Yield distribution by crop type
- Relationship between rainfall and yield
- Other relevant visualizations

## Project Structure

- `app.py` - Main application file
- `requirements.txt` - Project dependencies
- `crop_yield_train.csv` - Training dataset (to be provided by user)

## Future Scope

- Bluetooth/USB sensor integration
- Voice-based recommendations in local languages
- Android version with TensorFlow Lite
- Real-time weather alerts (when internet is available)

## License

This project is open-source and available under the MIT License. 