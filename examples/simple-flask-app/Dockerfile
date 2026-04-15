# ──────────────────────────────────────────────
# Step 1: Choose a base image
# ──────────────────────────────────────────────
FROM python:3.11-slim

# ──────────────────────────────────────────────
# Step 2: Set the working directory inside the container
# ──────────────────────────────────────────────
WORKDIR /app

# ──────────────────────────────────────────────
# Step 3: Copy dependency file and install packages
# ──────────────────────────────────────────────
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ──────────────────────────────────────────────
# Step 4: Copy the rest of the app files
# ──────────────────────────────────────────────
COPY . .

# ──────────────────────────────────────────────
# Step 5: Tell Docker which port the app uses
# ──────────────────────────────────────────────
EXPOSE 5000

# ──────────────────────────────────────────────
# Step 6: Start the application
# ──────────────────────────────────────────────
CMD ["python", "app.py"]
