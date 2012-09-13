function p = predict(Theta1, Theta2, X)
%PREDICT Predict the label of an input given a trained neural network
%   p = PREDICT(Theta1, Theta2, X) outputs the predicted label of X given the
%   trained weights of a neural network (Theta1, Theta2)

% Useful values
m = size(X, 1);

%t11, t12, t21, t22 = [25, 401], [10, 26] 
num_labels = size(Theta2, 1);
num_units = size(Theta1,1);

% [rows1, cols1] x [cols1, cols2] -> [rows1, cols2]

% add bias to data
X = [ones(m,1) X];

% a2 = g(X*Theta1)
a2 = zeros(m,num_units);

% a3 = g(Theta2*a2)
a3 = zeros(m, num_labels);

% You need to return the following variables correctly 
% the digits predicted (index of max value returned by max)
p = zeros(size(X, 1), 1);
% The max values returned by max
mx = zeros(size(X, 1), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Complete the following code to make predictions using
%               your learned neural network. You should set p to a 
%               vector containing labels between 1 to num_labels.
%
% Hint: The max function might come in useful. In particular, the max
%       function can also return the index of the max element, for more
%       information see 'help max'. If your examples are in rows, then, you
%       can use max(A, [], 2) to obtain the max for each row.
%

a2 = sigmoid(X*Theta1');
% add bias to hidden layer
a2 = [ones(m, 1) a2];
a3 = sigmoid(a2*Theta2');
% rhs should actually be max( sigmoid(a3, [], 2)) but sigmoid is monotonic, so 
[mx, p] = max( a3, [], 2);








% =========================================================================


end
