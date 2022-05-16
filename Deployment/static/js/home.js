$(document).ready(function (e) {
    // Waiting to run the submit in id: runModel
    $('#runModel').submit(function (event) {
        // Once it done the submit will erase the the tag with id: hfResult
        $('#hfResult').empty();

        // Collecting form values.
        var age = $('#age').val();
        var sex = $('#sex').val();
        var cp = $('#cp').val();
        var trestbps = $('#trestbps').val();
        var chol = $('#chol').val();
        var fbs = $('#fbs').val();
        var restecg = $('#restecg').val();
        var thalach = $('#thalach').val();
        var exang = $('#exang').val();
        var oldpeak = $('#oldpeak').val();
        var slope = $('#slope').val();
        var ca = $('#ca').val();
        var thal = $('#thal').val();


        // Inserting values into a javascript object
        var inputData = {
            'age': age,
            'sex': sex,
            'cp': cp,
            'trestbps': trestbps,
            'chol': chol,
            'fbs': fbs,
            'restecg': restecg,
            'thalach': thalach,
            'exang': exang,
            'oldpeak': oldpeak,
            'slope': slope,
            'ca': ca,
            'thal': thal
        };

        // Asynchronous request to the backend
        $.ajax({
            url: this.action,  // /main/api/run_model
            type: this.method, // POST
            data: inputData,
        })
        .done(function (response) { // Once the asynchronous request is successful, the command below will be executed
            if(response.pred == 0) {
                $('#hfResult').append(`<p>The Pacient does not have a Heart Disease</p>`) // Return to frontend if "predict" is 0
            } else {
                $('#hfResult').append(`<p>The Pacient has Heart Disease</p>`) // Return to frontend if "predict" is 1
            }
        });
        // Cancel default page refresh event
        event.preventDefault();
    });
});