# marinaGAN
This project is a DCGAN (Deep Convolutional Generative Adversarial Network) trained on a small dataset (<500 samples) of some of my portrait drawings. The training set is found [here](data-preproc/portraits). The images have been preprocessed to be 16x16 and in grayscale, and augmented to include horizontal flips (to maintain the context of the image).\
To help the training, I used a small training rate, an even smaller training rate for the discriminator, trained the discriminator slower that the generator, and used label smoothing. This was all done to make the discriminator's job a little harder as it had an advantage given the small dataset.

Reference: https://docs.pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html \
Used pytorch and training done in Colab 

<img src=gif/training_progress.gif/>

Because of the data constraints, the outputs ended up looking more like eldritch entities than faces. However, if we squint and look at it from a distance, they kind of resemble the training set :)

More: [Jupyter Notebook](GAN.ipynb)\
Demo: [HuggingFace Spaces](https://huggingface.co/spaces/mhmarina/marinaGAN)
