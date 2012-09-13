function val = multiLogLoss(y, p)
%MULTILOGLOSS Compute log loss = -1/m * sum({1,m}, sum({1,n}, I_y{i,j} * log (p{i,j}) ) )
% where I_y{i,j} is the indicator function

% Take a class index k and make it a row vector with 1 in the kth column

% Initialize some useful values
m = length(y); % = length(p(1)) = number of training examples

% y is m x 1, with values 1 to k
% p is m x k where k = number of classes

% You need to return the following variables correctly 
val = 0;

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

% for numerical stability, cap p between [10^-15, 1-10^-15]
p = max(min(p, 1-10^(-15)), 10^(-15));

val = (-1.0/m) * sum(y' * log(p) );


% =============================================================


end
