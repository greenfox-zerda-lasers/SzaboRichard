var selector = '[data-rangeSlider]',
        elements = document.querySelector(selector);
// Example functionality to demonstrate a value feedback

// Basic rangeSlider initialization
rangeSlider.create(elements, {
    min: 0,
    max: 5,
    value : 0,
    borderRadius : 3,
    buffer : 0,
    minEventInterval : 1000,
    // Callback function
    onInit: function () {
    },
    // Callback function
    onSlideStart: function (value, percent, position) {
        console.info('onSlideStart', 'value: ' + value, 'percent: ' + percent, 'position: ' + position);
    },
    // Callback function
    onSlide: function (value, percent, position) {
        console.log('onSlide', 'value: ' + value, 'percent: ' + percent, 'position: ' + position);
    },
    // Callback function
    onSlideEnd: function (value, percent, position) {
        console.warn('onSlideEnd', 'value: ' + value, 'percent: ' + percent, 'position: ' + position);
    }
});
