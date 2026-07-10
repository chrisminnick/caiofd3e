const stateButton = document.getElementById('oregonButton');
stateButton.addEventListener('click', () =>
  import('./bk07ch02_listing03.js').then((OregonInfo) => {
    alert(`${OregonInfo.stateName}'s state bird is ${OregonInfo.stateBird}.`);
  }),
);
