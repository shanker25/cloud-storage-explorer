Cloud Storage Explorer
Intern Details

•	Intern ID: CITS4540
•	Full Name: SHANKER A
•	No. of Weeks: 4
•	Project Name: Cloud Storage Explorer
________________________________________
Project Overview
Cloud Storage Explorer is a desktop application developed using Python, AWS S3, Boto3, and CustomTkinter. It provides a simple graphical interface for managing files stored in an Amazon S3 bucket. Users can upload, download, delete, refresh, and view files directly from the application.
________________________________________
Features
•	Upload files to Amazon S3
•	Download files from S3
•	Delete files from S3
•	Refresh bucket contents
•	Display file names and sizes
•	Modern dark-themed GUI using CustomTkinter
________________________________________
Technologies Used
•	Python 3
•	Amazon Web Services (AWS S3)
•	Boto3
•	CustomTkinter
•	Python-dotenv
________________________________________
Project Structure
cloud-storage-explorer/
│
├── app.py
├── README.md
├── requirements.txt
├── project-report.pdf
├── .gitignore
│
└── Screenshots/
    ├── user.png
    ├── upload.png
    ├── Interface.png
    ├── delete.png
    ├── bucket.png
________________________________________
Installation
1.	Clone the repository
git clone https://github.com/shanker25/cloud-storage-explorer.git
2.	Install dependencies
pip install -r requirements.txt
3.	Create a .env file
AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY
AWS_REGION=ap-southeast-2
BUCKET_NAME=YOUR_BUCKET_NAME
4.	Run the application
python app.py
________________________________________
Screenshots
Add the screenshots inside the Screenshots folder.
•	Home Screen
•	Upload File
•	Download File
•	Delete File
•	AWS S3 Bucket
________________________________________
Future Enhancements
•	Search functionality
•	File preview
•	Folder support
•	Progress bar
•	Storage usage dashboard
•	Drag-and-drop uploads
________________________________________
Conclusion
This project demonstrates the integration of Python desktop applications with AWS cloud storage services. It provides an easy-to-use interface for managing files in Amazon S3 while showcasing practical cloud computing concepts.
________________________________________
GitHub Repository
shanker25/cloud-storage-explorer
