def main():
    print("Hello World")
    print("This is the main file")
    print("The result of the perceptron input is", perceptron_input([ 1, 2, 3], [0.1, 0.2, 0.3], 0.4 ))

def perceptron_input ( inputs, weights, bias ):

    #:Calculate the perceptron input
    #:param inputs: List of inputs values
    #:param weights: List of weights corresponding to the inputs
    #:param bias: Bias Value 
    #:return The result of the weigthed sum of input plus the bias 

    weigthed_sum = sum( i * w for i, w in zip( inputs, weights))
    return weigthed_sum + bias 

def perceptron_output (inputs, weights, bias ):

    #:Calculate the perceptron output
    #:param inputs: List of inputs values 
    #:param weights: List of weights corresponding to the inputs
    #:param bias: Bias Value
    #:return: The output of the perceptron
    
    return 1 if perceptron_input (inputs, weights, bias ) >= 0 else 0

if __name__ == "_main_":
    main()
    