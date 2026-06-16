Lets assume logestic regression model is predicting for target value as 1
i.e p(y=1)=σ(z) where z = w1​x1​+w2​x2​+b 

### Without Regularization

I got: W=[16.76,−0.95] & b=−27.10

Here 16.76 is huge.

Suppose lets take a sample: x1​=2,x2​=3

Then z = 16.76(2)−0.95(3)−27.10 = 3.57

& prediction : σ(3.57)=0.972 => means 97.2% confident i.e. model predicts 97.2% correct as target 1

Now, if x1 = 3: z=20.33 & σ(20.33)≈0.999999998 => almost 100% 

This 100% is nothing but overfitting.

So we have to reduce the weights.

### With Regularization

I got: W=[0.397,0.044] & b=−0.70

Same sample: x1=2,x2=3

z=0.397(2)+0.044(3)−0.70

z=0.226

Prediction: σ(0.226)=0.556 => Only 55.6% (A good fit model)

### What is regularization doing?
Regularization add penalty to the cost when the weights are heigh

        J = Log Loss+ (λ/2m) (​∑ wj ** 2)​

Now the optimizer has two goals:
- Fit the data.
- Keep weights small.

If it makes w1=16.76,

it pays a penalty: (16.76)^2 = 280.9 => Huge cost.

If it keeps w1 = 0.397

penalty is: (0.397)^2 = 0.157 => Tiny cost.

#### Weights are not the only factor to check for overfitting, we have to compare with test data predictions. As this is toy dataset we can't split now. Only for regularization understanding purpose.