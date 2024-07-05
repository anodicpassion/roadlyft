<template>
  <div class="home">
    <p class="i" id="p"></p>
    <button id="b">Click me</button>
  </div>
</template>

<script>
function fuck_all(){
  document.getElementById("b").addEventListener("click", function() {
    document.getElementById("p").innerText = "Hello, world!";
});
}

export default {
  mounted() {
    fuck_all();
  }
};
</script>
