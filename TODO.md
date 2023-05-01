- [X] Choose 15 normal and 15 smiling images
- [X] Convert Images into grayscale
- [X] Convert images into vectors
- [X] Calculate the `average image vector`
    - Each column(feature) will be the average of all fearute values
- [X] Subtract the `average image vector` from every vector of the matrix to obtain the `zero mean vector`.
- [X] Apply PCA in `zero mean vector` to extract the `principal components matrix`.
- [X] Multiply `zero mean vector` against `principal components matrix` to the the `matrix of m most expressive features of each one of the N vectors`
  - [X] Stop and make an assesment of the closest images
- [X] Apply `MLDA` to the `matrix of m most expressive features of each one of the N vectors` to obtain the `m x 1 vector` 
- [X] Multiply the `matrix of m most expressive features of each one of the N vectors` against `m x 1 vector` to obtain the `most discriminant feature vector`
  - [X] Stop and make an assesment of the closest images