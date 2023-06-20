# Mapping global coordinates to local coordinates

Since we get global coordinates using:

$$
^\text{global}p 
~~~ =
~~~ ^\text{global}_\text{local}T
~~~ ^\text{local}p 
$$

then the reverse transform is literally the inverse of the homogeneous matrix:

$$
^\text{global}_\text{local}T^{-1}
~~~ ^\text{global}p 
~~~ =
~~~ ^\text{global}_\text{local}T^{-1}
~~~ ^\text{global}_\text{local}T
~~~ ^\text{local}p 
$$

$$
^\text{global}_\text{local}T^{-1}
~~~ ^\text{global}p 
~~~
=
~~~ ^\text{local}p 
$$
