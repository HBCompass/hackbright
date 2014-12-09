function fibonacci_set (max) {
    
    if (max > 1) 
    {

        var fib_array = [1];
        var current_fib = 1;
        for (var i = 1; i < max; i ++)
        {
            fib_array.push(current_fib);
            console.log(current_fib);
            current_fib = fib_array[fib_array.length -1] + fib_array[fib_array.length-2];
            
            console.log("This is the one",fib_array[fib_array.length-1]);
            console.log(current_fib);
            console.log(fib_array);
        }
        return fib_array;
    } else {
        return [1,1];
    }

    function sums_evens (fib_array) 
    {
        var sum = 0;
        for (var i = 0; i < len(fib_array); i++)
        {
            if (i %2 === 0) 
            {
                sum += i;

                console.log(sum);
            }
    
        }
        return sum;
    }
}

console.log( fibonacci_set(40));