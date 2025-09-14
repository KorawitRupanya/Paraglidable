# Base image
FROM tensorflow/tensorflow:latest-gpu

# Arguments
ARG USERNAME=paraglidable

# Ensure root for installing system packages and user creation
USER root

# Install adduser and sudo if missing
RUN apt-get update && apt-get install -y --no-install-recommends \
    adduser sudo \
    net-tools \
    libopenjp2-7-dev \
    libpng-dev \
    libpng16-16 \
    vim \
    sass \
    wget \
    qt5-default \
    pdf2svg \
    apache2 \
    php \
    libapache2-mod-php \
    nodejs \
    npm \
    libgrib-api-dev \
    unzip \
    libgeos-dev \
    libproj-dev \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN adduser --disabled-password --gecos "" $USERNAME \
    && echo "$USERNAME ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Set environment
ENV HOME=/home/$USERNAME
ENV DEBIAN_FRONTEND=noninteractive
ENV NPY_DISABLE_CPU_FEATURES=AVX,AVX2,FMA

# Switch to non-root user
USER $USERNAME
WORKDIR $HOME

# Upgrade pip
RUN pip install --upgrade pip

# Install basemap 1.2.1 from GitHub tarball
RUN pip install --no-cache-dir https://github.com/matplotlib/basemap/archive/v1.2.1rel.tar.gz

# Copy Python requirements
COPY python_requirements.txt .

# Install Python packages with sudo (non-root)
RUN sudo pip install --no-cache-dir -r python_requirements.txt
