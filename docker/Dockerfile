# Base image: NVIDIA L4T TensorFlow (ARM64, GPU-enabled)
FROM nvcr.io/nvidia/l4t-tensorflow:r35.3.1-tf2.11-py3

# Arguments
ARG USERNAME=paraglidable

# Switch to root to install system packages and create user
USER root

# Set environment variables
ENV HOME=/home/$USERNAME
ENV DEBIAN_FRONTEND=noninteractive
ENV NPY_DISABLE_CPU_FEATURES=AVX,AVX2,FMA

# Update apt and install essential packages
# Install system deps for PyGObject / Cairo
RUN apt-get update && apt-get install -y \
    python3-gi \
    gir1.2-gtk-3.0 \
    libcairo2-dev \
    pkg-config \
    python3-cairo \
    gobject-introspection \
    libgirepository1.0-dev \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN adduser --disabled-password --gecos "" $USERNAME \
    && echo "$USERNAME ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Switch to non-root user
USER $USERNAME
WORKDIR $HOME

# Upgrade pip
RUN pip install --upgrade pip

# Install basemap 1.2.1 from GitHub
RUN pip install --no-cache-dir https://github.com/matplotlib/basemap/archive/v1.2.1rel.tar.gz

# Copy Python requirements
COPY python_requirements.txt .

# Install Python packages with sudo
RUN sudo pip install --no-cache-dir -r python_requirements.txt

# Default command
CMD ["/bin/bash"]
