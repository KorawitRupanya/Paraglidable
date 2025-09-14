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
RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-utils \
    sudo \
    adduser \
    net-tools \
    vim \
    wget \
    unzip \
    python3-pip \
    libopenjp2-7-dev \
    libpng-dev \
    libgeos-dev \
    libproj-dev \
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
