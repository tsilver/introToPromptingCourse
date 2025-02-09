# AIxponential Prompting Course

An interactive course teaching AI prompting techniques, from fundamentals to advanced applications.

## 🎯 Course Overview

This course teaches you how to effectively communicate with AI language models through:
- Fundamental prompting techniques
- Advanced interaction methods
- Ethical considerations
- Practical applications

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/prompting-course.git
cd prompting-course
```

2. Create a virtual environment:
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Required packages include:
- Core: streamlit, python-dotenv, requests
- Visualization: plotly
- UI: streamlit-extras
- Development: black, pylint, pytest
- Documentation: mkdocs, mkdocs-material
- Utilities: python-slugify, pyyaml

4. Set up environment variables:
```bash
# Create .env file
touch .env

# Add your API keys to .env
OPENAI_API_KEY=your_openai_api_key
```

### Running the Course

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to:
```
http://localhost:8501
```

## 📚 Course Structure

### Module 1: Fundamentals of Prompting
- Basic prompt components
- Context and constraints
- Explanation techniques
- Conversation management

### Module 2: Advanced Techniques
- Few-shot prompting
- Role-based approaches
- Structured outputs
- Iterative refinement

### Module 3: Critical Thinking & Ethics
- Bias identification
- Hallucination detection
- Ethical principles
- Responsible implementation

## 🛠️ Features

- Interactive exercises
- Real-time feedback
- Progress tracking
- Comprehensive analytics
- Course completion certificate

## 📋 Requirements

See `requirements.txt` for a full list of dependencies. Key requirements include:
- streamlit>=1.31.0
- plotly>=5.18.0
- python-dotenv>=1.0.0
- requests>=2.31.0

## 🤝 Contributing

Interested in contributing? Please read our contributing guidelines and submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for API access
- Streamlit for the web framework
- All contributors and testers

## 📞 Support

For support, please:
1. Check the documentation
2. Search existing issues
3. Create a new issue if needed

## 🔄 Updates

Stay updated with the latest course content and features by following our repository. 