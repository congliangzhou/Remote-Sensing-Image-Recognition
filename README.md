# Remote-Sensing-Image-Recognition
Application of Convolutional Neural Network in Remote Sensing Image Recognition


1. Split the Texas Image and convert it to tiles. 
2.Start Docker with local files available
% docker run -it -v $HOME/tf_files:/tf_files  gcr.io/tensorflow/tensorflow:latest-devel        # my file: /tf_filesclassification/evergreen forest, shrub_scrub, cultivated_crops
3.Retrieving the training code
  # cd /tensorflow
  # git pull
4.Start your image retraining 
# python tensorflow/examples/image_retraining/retrain.py \                  # retrain contains the code used to train image classification
--bottleneck_dir=/tf_files/bottlenecks \
--how_many_training_steps 500 \
--model_dir=/tf_files/inception \
--output_graph=/tf_files/retrained_graph.pb \
--output_labels=/tf_files/retrained_labels.txt \
--image_dir /tf_files/classification
5.use the label_image.py to load my graph file and predicts with it. I put label_image.py in the folder of ty_files.
# python /tf_files/label_image.py /tf_files/testpicture/*picture name

