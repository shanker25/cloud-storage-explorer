import customtkinter as ctk
from tkinter import filedialog, messagebox
from dotenv import load_dotenv
import boto3
import os

# -------------------------------
# Load Environment Variables
# -------------------------------
load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("BUCKET_NAME")

# -------------------------------
# AWS S3 Client
# -------------------------------
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

# -------------------------------
# GUI Settings
# -------------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("950x650")
app.title("Cloud Storage Explorer")

title = ctk.CTkLabel(
    app,
    text="☁ Cloud Storage Explorer",
    font=("Arial", 28, "bold")
)
title.pack(pady=15)

bucket_label = ctk.CTkLabel(
    app,
    text=f"Bucket : {BUCKET_NAME}",
    font=("Arial", 15)
)
bucket_label.pack()

textbox = ctk.CTkTextbox(
    app,
    width=750,
    height=320
)
textbox.pack(pady=20)

status = ctk.CTkLabel(
    app,
    text="Ready",
    font=("Arial", 14)
)
status.pack(pady=5)


def refresh_files():
    textbox.delete("1.0", "end")

    try:
        print("Bucket:", BUCKET_NAME)
        print("Region:", AWS_REGION)

        response = s3.list_objects_v2(Bucket=BUCKET_NAME)

        print(response)

        if "Contents" not in response:
            textbox.insert("end", "Bucket is empty.")
            status.configure(text="Bucket is empty")
            return

        for obj in response["Contents"]:
            textbox.insert(
                "end",
                f"{obj['Key']}    {obj['Size']} bytes\n"
            )

        status.configure(text="Files refreshed")

    except Exception as e:
        print(e)
        raise

# -------------------------------
# Upload File
# -------------------------------
def upload_file():
    file_path = filedialog.askopenfilename()

    if not file_path:
        return

    try:
        filename = os.path.basename(file_path)

        s3.upload_file(
            file_path,
            BUCKET_NAME,
            filename
        )

        messagebox.showinfo(
            "Success",
            f"{filename} uploaded successfully!"
        )

        refresh_files()

    except Exception as e:
        messagebox.showerror("Upload Error", str(e))


# -------------------------------
# Download File
# -------------------------------
def download_file():

    filename = textbox.get("insert linestart", "insert lineend").split(" ")[0]

    if filename == "":
        messagebox.showwarning(
            "Warning",
            "Select a file name from the list."
        )
        return

    save_path = filedialog.asksaveasfilename(
        initialfile=filename
    )

    if not save_path:
        return

    try:

        s3.download_file(
            BUCKET_NAME,
            filename,
            save_path
        )

        messagebox.showinfo(
            "Success",
            "File downloaded successfully."
        )

    except Exception as e:
        messagebox.showerror("Download Error", str(e))


# -------------------------------
# Delete File
# -------------------------------
def delete_file():

    filename = textbox.get("insert linestart", "insert lineend").split(" ")[0]

    if filename == "":
        messagebox.showwarning(
            "Warning",
            "Select a file."
        )
        return

    confirm = messagebox.askyesno(
        "Delete",
        f"Delete {filename} ?"
    )

    if not confirm:
        return

    try:

        s3.delete_object(
            Bucket=BUCKET_NAME,
            Key=filename
        )

        messagebox.showinfo(
            "Deleted",
            f"{filename} deleted."
        )

        refresh_files()

    except Exception as e:
        messagebox.showerror("Delete Error", str(e))
    
# -------------------------------
# Buttons
# -------------------------------

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=20)

upload_btn = ctk.CTkButton(
    button_frame,
    text="📤 Upload",
    width=150,
    command=upload_file
)
upload_btn.grid(row=0, column=0, padx=10)

download_btn = ctk.CTkButton(
    button_frame,
    text="📥 Download",
    width=150,
    command=download_file
)
download_btn.grid(row=0, column=1, padx=10)

delete_btn = ctk.CTkButton(
    button_frame,
    text="🗑 Delete",
    width=150,
    command=delete_file
)
delete_btn.grid(row=0, column=2, padx=10)

refresh_btn = ctk.CTkButton(
    button_frame,
    text="🔄 Refresh",
    width=150,
    command=refresh_files
)
refresh_btn.grid(row=0, column=3, padx=10)

# -------------------------------
# Footer
# -------------------------------

footer = ctk.CTkLabel(
    app,
    text="Built with Python • AWS S3 • CustomTkinter",
    font=("Arial", 12)
)
footer.pack(pady=10)

# -------------------------------
# Load Files on Startup
# -------------------------------

refresh_files()

# -------------------------------
# Run Application
# -------------------------------

app.mainloop()