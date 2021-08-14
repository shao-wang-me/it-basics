# Radio Button

<fieldset>
  <label>
    <input type="radio" name="季节"/>
    春
  </label>
  <label>
    <input type="radio" name="季节"/>
    秋
  </label>
</fieldset>
<style>
  input[type="radio"] {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    border-radius: 50%;
    width: 24px;
    height: 24px;
    border: 1px solid #B8B8C4;
    transition: 0.2s all linear;
    margin-right: 5px;
    position: relative;
    top: 4px;
  }
  input:hover {
    border: 1px solid #808090;
  }
  input[type="radio"]:checked {
    border: initial;
    background: #008DEF;
  }
  input[type="radio"]:checked::after {
    position: absolute;
    content: "";
    top: 6px;
    left: 6px;
    height: 12px;
    width: 12px;
    background: white;
    border-radius: 50%;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
  }
</style>
