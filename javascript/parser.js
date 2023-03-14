var input_str = "wb: 1.23, other: 15.000000, something: 0.9";
// parse string into hash of key value pairs
function parse_string(input_str) {
    var input_arr = input_str.split(", ");
    var input_hash = {};
    for (var i = 0; i < input_arr.length; i++) {
        var key_val = input_arr[i].split(": ");
        input_hash[key_val[0]] = key_val[1];
    }
    return input_hash;
}
function test_functions() {
    console.log(parse_string(input_str));
}
test_functions();
