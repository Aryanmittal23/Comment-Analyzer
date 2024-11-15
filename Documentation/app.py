import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Comment Analyzer - YouTube Insights",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)
# Function to load Lottie animations from URL
def load_lottieurl(url: str):
    """
    Loads a Lottie animation from a URL.

    Parameters:
        url (str): The URL of the Lottie JSON file.

    Returns:
        dict: The Lottie animation JSON data.
    """
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Define each page as a separate function
def home():
    st.title("📊 **Welcome to Comment Analyzer!**")
    st.markdown("### Gain Insights from YouTube Comments")
    st.write("---")

    # Load and display a Lottie animation
    lottie_animation = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_u4yrau.json")  # Update with relevant Lottie link
    if lottie_animation:
        st_lottie(lottie_animation, height=300, key="home_animation")

    st.markdown("""
    **Comment Analyzer** is a powerful tool to analyze and extract insights from YouTube comments. Whether you're a content creator, marketer, or researcher, this tool helps you make data-driven decisions by understanding audience feedback.
    """)

    st.write("---")
    st.header("🔍 **Key Features**")
    st.markdown("""
    - **Sentiment Analysis**: Understand the emotions conveyed in comments (positive, negative, neutral).
    - **Keyword Extraction**: Identify frequently mentioned topics or phrases.
    - **Trend Analysis**: Track how sentiments and keywords evolve over time.
    - **Word Clouds**: Visualize key themes in the comments.
    - **Engagement Metrics**: Analyze the frequency and length of comments.
    """)

    st.write("---")
    st.header("🚗 **How It Works**")
    with st.expander("📥 Fetch Comments"):
        st.markdown("""
        1. **Input YouTube Video Link**: Paste the link to the YouTube video.
        2. **Fetch Comments**: The tool retrieves comments using YouTube's API.
        """)

    with st.expander("📊 Analyze Data"):
        st.markdown("""
        1. **Sentiment Analysis**: Determine the tone of comments (positive, negative, neutral).
        2. **Keyword Extraction**: Highlight frequently used words or phrases.
        3. **Visualizations**: View insights through graphs and word clouds.
        """)

    st.write("---")
    st.header("🔗 **Get Started**")
    st.markdown("""
    Ready to unlock insights from YouTube comments? **[Start Analyzing Now](#)** and turn feedback into actionable data.
    """)

    st.button("🚀 **Analyze Comments**", help="Click to begin analyzing comments from a YouTube video!")

def frontend():
    st.title("🚀 **Frontend Documentation**")
    st.write("---")

    st.subheader("📝 **Design Considerations**")
    st.markdown("""
    The frontend of the **Comment Analyzer** project was designed with several key considerations in mind:

    - **User-Centric Design**: The interface prioritizes ease of use, ensuring users can input YouTube video links and view analysis results effortlessly.
    - **Responsive Layout**: The application is fully responsive, offering a seamless experience across devices such as desktops, tablets, and mobile phones.
    - **Accessibility**: Adherence to accessibility standards ensures inclusivity for all users, including those with disabilities.
    - **Performance Optimization**: The frontend is optimized for fast load times and smooth interactions, especially when displaying data visualizations.
    """)

    st.subheader("✨ **Key Features**")
    st.markdown("""
    The frontend of **Comment Analyzer** includes several notable features:

    - **YouTube API Integration**: Users can fetch and analyze comments by providing a YouTube video link.
    - **Sentiment Analysis Results**: Display a summary of sentiment (positive, negative, neutral) with corresponding visualizations.
    - **Keyword Extraction**: Showcase the most frequently used words in a word cloud.
    - **Interactive Charts**: Visualize sentiment trends and engagement metrics through charts.
    - **Dynamic Content Loading**: The interface dynamically updates with results after the analysis is completed.
    """)

    st.subheader("🛠️ **Technological Stack**")
    st.markdown("""
    The **Comment Analyzer** frontend utilizes a modern technological stack:

    - **React**: A JavaScript library for building user interfaces with reusable components.
    - **Vite**: A build tool that provides a fast development environment with hot module replacement (HMR).
    - **Material UI**: A React UI framework offering pre-designed components for a consistent look.
    - **Chart.js**: A library for creating dynamic and interactive charts to visualize sentiment trends and keyword analysis.
    - **React Router**: A routing library for navigation between views in the application.
    """)

    st.subheader("📄 **Technical Documentation**")
    st.markdown("""
    **Project Structure:**

    ```
    comment-analyzer/
    ├── eslint.config.js
    ├── index.html
    ├── package-lock.json
    ├── package.json
    ├── public/
    │   └── logo.png
    ├── README.md
    ├── src/
    │   ├── App.css
    │   ├── App.jsx
    │   ├── assets/
    │   │   └── analysis-icon.png
    │   ├── components/
    │   │   ├── SentimentChart.jsx
    │   │   ├── WordCloud.jsx
    │   │   └── Navbar.jsx
    │   ├── hooks/
    │   │   └── useYouTubeComments.jsx
    │   ├── index.css
    │   ├── main.jsx
    │   └── vite.config.js
    ```

    **Key Files:**

    1. `index.html`: Entry point of the application, containing meta tags for responsiveness and links to the main JavaScript file.

    ```html
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <link rel="icon" href="/logo.png" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Comment Analyzer</title>
    </head>
    <body>
        <div id="root"></div>
        <script type="module" src="/src/main.jsx"></script>
    </body>
    </html>
    ```

    2. `main.jsx`: Initializes the React application and renders it into the DOM.

    ```javascript
    import React from 'react';
    import ReactDOM from 'react-dom';
    import { BrowserRouter } from 'react-router-dom';
    import App from './App';
    import './index.css';

    ReactDOM.createRoot(document.getElementById('root')).render(
        <BrowserRouter>
            <App />
        </BrowserRouter>
    );
    ```

    3. `App.jsx`: The root component managing routing and layout.

    ```javascript
    import React from 'react';
    import { Routes, Route } from 'react-router-dom';
    import Home from './pages/Home';
    import Analysis from './pages/Analysis';
    import Dashboard from './pages/Dashboard';

    const App = () => {
        return (
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/analysis" element={<Analysis />} />
                <Route path="/dashboard" element={<Dashboard />} />
            </Routes>
        );
    };

    export default App;
    ```

    4. **Pages Directory (`src/pages/`)**: Contains components for different pages, such as `Home` for inputting the YouTube link and `Analysis` for displaying results.

    5. **Components Directory (`src/components/`)**: Includes reusable UI elements like `SentimentChart` and `WordCloud`.

    6. **Utils Directory (`src/utils/`)**: Contains helper functions for fetching comments, performing sentiment analysis, and extracting keywords.

    **Styling**

    - The application uses **CSS Modules** for scoped styles and **Material UI** for consistent UI components.

    **ESLint Configuration**

    The project uses **ESLint** to maintain code quality and enforce consistent coding standards.

    ```javascript
    module.exports = {
        extends: ["react-app", "react-app/jest"],
        rules: {
            "react-hooks/exhaustive-deps": "warn",
            "no-console": "warn",
        },
    };
    ```

    **Conclusion**

    The frontend for **Comment Analyzer** is built with a modern tech stack and focuses on performance, responsiveness, and user engagement. Its modular structure and reusable components ensure scalability and maintainability.
    """)

def backend():
    st.title("🚀 **Backend Documentation**")
    st.write("---")

    st.subheader("🔧 **Design Considerations**")
    st.markdown("""
    The backend of the **Comment Analyzer** project was developed with several design considerations to ensure robustness, scalability, and security:

    - **Modular Architecture**: Structured in a modular fashion, allowing for easy maintenance and scalability. Each component (controllers, models, routes) is separated to enhance code readability and organization.
    - **Security**: Implementing JWT (JSON Web Tokens) for authentication ensures that user sessions are secure. Additionally, sensitive data is managed through environment variables using dotenv.
    - **API Integration**: Integrates with YouTube's API to fetch comments efficiently, handling rate limits and ensuring data consistency.
    - **Database Connection Management**: Utilizes Mongoose for MongoDB interactions, ensuring efficient database connection handling and schema validation.
    - **Error Handling**: Comprehensive error handling mechanisms are implemented to provide meaningful responses to the client while logging errors for debugging purposes.
    - **Scalability**: Designed to handle large volumes of comments and analysis requests, ensuring the application can scale horizontally as needed.
    """)

    st.subheader("✨ **Key Features**")
    st.markdown("""
    The backend of **Comment Analyzer** includes several essential features:

    - **User Authentication**: Users can register and log in securely, with their credentials stored safely in the database.
    - **YouTube API Integration**: Fetches comments from YouTube videos using the YouTube Data API, handling pagination and rate limits.
    - **Comment Storage**: Stores fetched comments in the database for efficient retrieval and analysis.
    - **Sentiment Analysis**: Processes comments to determine their sentiment (positive, negative, neutral) using NLP techniques.
    - **Keyword Extraction**: Identifies and stores frequently mentioned keywords and phrases from the comments.
    - **Analysis Results Management**: Stores and retrieves analysis results, enabling users to view historical data and trends.
    - **API Endpoints**: Provides RESTful API endpoints for frontend interactions, including fetching comments, initiating analysis, and retrieving results.
    """)

    st.subheader("🛠️ **Technological Stack**")
    st.markdown("""
    The backend of **Comment Analyzer** employs a modern technological stack:

    - **Node.js**: A JavaScript runtime that allows for server-side scripting.
    - **Express.js**: A web application framework for Node.js that simplifies routing and middleware management.
    - **MongoDB**: A NoSQL database used for storing user data, comments, and analysis results.
    - **Mongoose**: An ODM (Object Data Modeling) library for MongoDB that provides schema-based solutions to model application data.
    - **YouTube Data API v3**: Used to fetch comments from YouTube videos.
    - **Natural Language Processing (NLP) Libraries**: Libraries such as **Sentiment** or **Natural** for performing sentiment analysis and keyword extraction.
    - **JWT (JSON Web Tokens)**: Used for secure authentication.
    - **dotenv**: For managing environment variables securely.
    """)

    st.subheader("📄 **Technical Documentation**")
    st.markdown("""
    **Project Structure:**

    ```
    backend
    ├── app.js
    ├── controller/
    │   ├── AuthController.js
    │   ├── CommentController.js
    │   └── AnalysisController.js
    ├── middleware/
    │   └── fetchuser.js
    ├── models/
    │   ├── User.js
    │   ├── Comments.js
    │   └── UrlModel.js
    ├── routers/
    │   ├── auth.js
    │   └── comments.js
    ├── package-lock.json
    ├── package.json
    └── .env
    ```

    **Key Files:**

    1. `app.js`: The main entry point of the application that initializes the server, connects to the database, and sets up middleware and routes.

    ```javascript
    import express from "express";
    import dotenv from "dotenv";
    import cookieParser from "cookie-parser";
    import connectDB from "./db/connectDB.js";
    import authRoutes from "./routes/authRoutes.js";
    import commentRoutes from "./routes/commentRoutes.js";
    import analysisRoutes from "./routes/analysisRoutes.js";
    import { errorHandler } from "./middleware/errorHandler.js";

    dotenv.config();
    connectDB();

    const app = express();
    app.use(cookieParser());
    app.use(express.json({ limit: "50mb" }));
    app.use(express.urlencoded({ extended: true }));

    // Routes
    app.use("/api/auth", authRoutes);
    app.use("/api/comments", commentRoutes);
    app.use("/api/analysis", analysisRoutes);

    // Error Handling Middleware
    app.use(errorHandler);

    const PORT = process.env.PORT || 5000;
    app.listen(PORT, () => {
        console.log(`Server started on port ${PORT}`);
    });
    ```

    2. **Controllers:**
       - `AuthController.js`: Manages user registration, login, and authentication.
       - `CommentController.js`: Handles fetching comments from YouTube and storing them in the database.
       - `AnalysisController.js`: Performs sentiment analysis and keyword extraction on stored comments.

       **Example: `CommentController.js`**

       ```javascript
       import YouTubeService from "../services/youtubeService.js";
       import Comment from "../models/Comment.js";

       // Fetch and store comments from a YouTube video
       export const fetchComments = async (req, res, next) => {
           try {
               const { videoId } = req.params;
               const comments = await YouTubeService.getComments(videoId);

               // Save comments to the database
               const savedComments = await Comment.insertMany(comments);

               res.status(200).json({ success: true, data: savedComments });
           } catch (error) {
               next(error);
           }
       };
       ```

    3. **Models (`models/`):**
       - `User.js`: Defines the User schema with fields like username, email, password, etc.
       - `Comments.js`: Defines the Comment schema including details like comment text, author, timestamp, sentiment score, etc.
       

       **Example: `Comments.js`**

       ```javascript
       import mongoose from "mongoose";

       const CommentSchema = new mongoose.Schema({
           videoId: {
               type: String,
               required: true,
           },
           author: {
               type: String,
               required: true,
           },
           text: {
               type: String,
               required: true,
           },
           publishedAt: {
               type: Date,
               required: true,
           },
           sentiment: {
               type: String,
               enum: ["positive", "negative", "neutral"],
               default: "neutral",
           },
           keywords: {
               type: [String],
               default: [],
           },
       });

       export default mongoose.model("Comment", CommentSchema);
       ```

    4. **Middleware (`middleware/`):**
       - `fetchuser.js`: Verifies JWT tokens to protect secure routes.
       
       **Example: `fetchuser.js`**

       ```javascript
       import jwt from "jsonwebtoken";
       import User from "../models/User.js";

       const authenticate = async (req, res, next) => {
           const token = req.cookies.token || "";

           if (!token) {
               return res.status(401).json({ message: "No token provided, authorization denied" });
           }

           try {
               const decoded = jwt.verify(token, process.env.JWT_SECRET);
               req.user = await User.findById(decoded.id).select("-password");
               next();
           } catch (error) {
               res.status(401).json({ message: "Token is not valid" });
           }
       };

       export default authenticate;
       ```

    5. **Routers (`routers/`):**
       - `auth.js`: Defines routes for user authentication (e.g., `/register`, `/login`).
       - `comments.js`: Defines routes for fetching and managing comments (e.g., `/fetch/:videoId`).
       

       **Example: `comments.js`**

       ```javascript
       import express from "express";
       import { fetchComments } from "../controller/CommentController.js";
       import authenticate from "../middleware/authenticate.js";

       const router = express.Router();

       // Fetch comments for a specific YouTube video
       router.get("/fetch/:videoId", authenticate, fetchComments);

       export default router;
       ```

    **Styling**

    - The backend does not involve direct styling; however, clear and consistent API responses and error messages are maintained to ensure ease of integration with the frontend.

    **ESLint Configuration**

    The project uses **ESLint** to maintain code quality and enforce consistent coding standards.

    ```javascript
    module.exports = {
        env: {
            browser: false,
            node: true,
            es2021: true,
        },
        extends: ["eslint:recommended", "plugin:react/recommended"],
        parserOptions: {
            ecmaVersion: 12,
            sourceType: "module",
        },
        plugins: ["react"],
        rules: {
            "no-unused-vars": "warn",
            "no-console": "off",
            "semi": ["error", "always"],
            "quotes": ["error", "single"],
        },
    };
    ```

    **Conclusion**

    This documentation provides a comprehensive overview of the backend design considerations, key features, technological stack, and technical structure of the **Comment Analyzer** project. By adhering to these guidelines and utilizing modern technologies, the project aims to create a secure, efficient, and scalable platform for analyzing YouTube comments, providing valuable insights through sentiment analysis and keyword extraction.
    """)


def machine_learning_documentation():
    st.title("🧠Machine Learning Documentation")
    st.write("---")

    st.subheader("🔬 **Design Considerations**")
    st.markdown("""
    The machine learning models for **Comment Analyzer** were developed with the following considerations:

    - **Data Quality and Preprocessing**: Emphasis on cleaning, tokenizing, and normalizing comment text to improve model accuracy.
    - **Model Selection**: Support Vector Machines (SVM) for sentiment classification, optimized for short text comments.
    - **Scalability**: Designed to handle a growing dataset of YouTube comments efficiently, ensuring minimal latency in predictions.
    - **Performance Monitoring**: Regular evaluation of precision, recall, and F1 scores to maintain high performance.
    """)

    st.subheader("✨ **Key Features**")
    st.markdown("""
    The **Comment Analyzer** machine learning components include:

    - **Sentiment Analysis**: Predicts whether comments are positive, negative, or neutral, providing actionable insights.
    - **YouTube API Integration**: Automatically fetches comments from a given YouTube video using its video ID.
    - **Scalable Architecture**: Models are served through Flask APIs, allowing integration with web or mobile interfaces.
    """)

    st.subheader("🛠️ **Technological Stack**")
    st.markdown("""
    - **Python**: Programming language for model development and deployment.
    - **scikit-learn**: Used for training and deploying the sentiment analysis model.
    - **Flask**: Serves the ML model and API endpoints.
    - **YouTube API v3**: Fetches comments for analysis from YouTube videos.
    """)

    st.subheader("📄 **Technical Documentation**")
    st.markdown("""
    **Project Structure:**

    ```
    CommentAnalyzer/
    ├── app.py  # Flask application
    ├── svm_model.joblib  # Pre-trained sentiment analysis model
    ├── comment_fetcher.py  # Module for YouTube API integration
    ├── sentiment_predictor.py  # Module for sentiment analysis
    └── requirements.txt  # Dependencies
    ```

    ### Components Overview

    1. **YouTube Comments Fetcher (`comment_fetcher.py`)**
       - **Purpose**: Fetches comments from YouTube videos using the YouTube API v3.
       - **Example Usage**:
       ```python
       video_id = "abc123"
       comments = get_youtube_comments(video_id)
       ```
       - **Code Implementation**:
       ```python
       import googleapiclient.discovery

       def get_youtube_comments(video_id, max_results=100):
           youtube = googleapiclient.discovery.build("youtube", "v3", developerKey="YOUR_API_KEY")
           request = youtube.commentThreads().list(
               part="snippet",
               videoId=video_id,
               maxResults=max_results
           )
           response = request.execute()
           comments = [item['snippet']['topLevelComment']['snippet']['textDisplay'] for item in response.get('items', [])]
           return comments
       ```

    2. **Sentiment Analysis Model (`sentiment_predictor.py`)**
       - **Purpose**: Predicts sentiment of comments (Positive, Negative, Neutral).
       - **Technology**: SVM model trained on labeled comment data.
       - **Example Usage**:
       ```python
       comments = ["Great video!", "Not helpful."]
       sentiments = predict_sentiment(comments)
       ```
       - **Code Implementation**:
       ```python
       import joblib

       # Load pre-trained SVM model
       svm_model = joblib.load("svm_model.joblib")

       def predict_sentiment(comments):
           predictions = svm_model.predict(comments)
           return predictions
       ```

    3. **Flask Application (`app.py`)**
       - **Purpose**: Exposes RESTful APIs for fetching YouTube comments and performing sentiment analysis.
       - **Endpoints**:
         - `/get_comments`: Fetches comments for a given YouTube video ID.
         - `/predict_sentiment`: Predicts sentiment for a list of comments.
       - **Code Implementation**:
       ```python
       from flask import Flask, request, jsonify
       from comment_fetcher import get_youtube_comments
       from sentiment_predictor import predict_sentiment

       app = Flask(__name__)

       @app.route('/get_comments', methods=['POST'])
       def get_comments():
           data = request.get_json()
           video_id = data.get('videoId')
           comments = get_youtube_comments(video_id)
           return jsonify(comments)

       @app.route('/predict_sentiment', methods=['POST'])
       def predict_sentiment_endpoint():
           data = request.get_json()
           comments = data.get('comments', [])
           sentiments = predict_sentiment(comments)
           return jsonify(sentiments)

       if __name__ == "__main__":
           app.run(port=5000, debug=True)
       ```

    ### Model Training and Evaluation

    - **Dataset**: Labeled YouTube comments dataset for sentiment classification.
    - **Algorithm**: Support Vector Machines (SVM) with TF-IDF vectorization.
    - **Metrics**: 
        - **Accuracy**: 85%
        - **Precision**: 82%
        - **Recall**: 80%
    """)

    st.subheader("📌 **Future Improvements**")
    st.markdown("""
    - **Multilingual Support**: Extend sentiment analysis to handle comments in multiple languages.
    - **Enhanced Visualization**: Add data visualizations to represent sentiment distributions effectively.
    - **Integration with Other Platforms**: Extend support to analyze comments from Twitter, Facebook, etc.
    """)


def main():
    # Sidebar Navigation
    st.sidebar.title("🔎 **Explore Comment Analyser**")
    pages = {
        "Home": home,
        "Frontend": frontend,
        "Backend": backend,
        "Machine Learning": machine_learning_documentation
        # "Investor Pitch": investor_pitch,  # Include other pages if necessary
    }
    selected_page = st.sidebar.selectbox("Navigate to:", options=list(pages.keys()))
    st.sidebar.write("---")
    st.sidebar.write("©️ 2024 Comment Analyzer")

    # Display the selected page with some padding
    st.markdown(
        """
        <style>
        .reportview-container .main .block-container{
            padding-top: 1rem;
            padding-right: 2rem;
            padding-left: 2rem;
            padding-bottom: 2rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    pages[selected_page]()  # Call the function for the selected page

if __name__ == "__main__":
    main()