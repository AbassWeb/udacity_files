
// store variable data
sizePicker.addEventListener("submit", ()=>{
    makeGrid(height, width);
})

    var table = document.getElementById("pixelCanvas");
    var height = document.getElementById("inputHeight");
    var width = document.getElementById("inputWidth");
    var color = document.getElementById("colorPicker");
    var size = document.getElementById("sizePicker");


    // add / remove grid into table element
    // no new page created
    document.addEventListener('click', function (event) {
        event.preventDefault();
    	  	  makeGrid(inputHeight, inputWidth);

    });


    // loop over each row
    // make grid
    // h=height, w=width
    // pix=paintable square
function makeGrid(inputHeight, InputWidth) {
    table.innerHTML = "";

    for (let h = 0; h < inputHeight.value; h++) {
      let row = table.insertRow(h);
    for (let w = 0; w < inputWidth.value; w++) {
      let cell = row.insertCell(w);

      row.appendChild(cell);

    table.appendChild(row);

    };
  };
};
