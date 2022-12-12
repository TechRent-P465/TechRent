<template>
        <!-- <label for="ref" style="position: fixed; top:300px; left" >Why do you need a refund? </label><br> -->
  <!-- <input type="text" style="position: fixed; top:400px;" id="ref" name="ref"><br><br> -->
  <div class="form-container">
  <h1>Request a refund</h1>

  <form>
  <div class="form-group row">
    <label for="name" class="col-sm-2 col-form-label1"><h3>Name:</h3></label>
    <div class="col-sm-5"><br/>
      <input type="text" class="form-control1" id="name" placeholder="Enter your name" v-model="refundItem.name">
    </div>
  </div>
  <div class="form-group row">
    <label for="email" class="col-sm-2 col-form-label2"><h3>Email:</h3></label>
    <div class="col-sm-5"><br/>
      <input type="email" class="form-control2" id="email" placeholder="Enter your email address" v-model="refundItem.email">
    </div>
  </div>
  <div class="form-group row">
    <label for="refund" class="col-sm-2 col-form-label"><h3>Why do you need a refund?</h3></label>
    <div class="col-sm-5"><br/>
      <input type="text" class="form-control" id="refund" placeholder="Brief explanation is required" v-model="refundItem.question1">
    </div>
  </div>
    <div class="col-auto my-1">
      <button type="submit" @click="myFunction" class="btn btn-primary">Submit</button>
    </div>
</form>
</div>
</template>

<script>
export default {
data () {
  return {
    refundItem: {
      name: '',
      email: '',
      question1: ''
    }
  }
},
methods: {
  myFunction () {
    let text = "We will notify you if the refund request is approved!";
    if (confirm(text) == true) {
      text = "You pressed OK!";
      this.$store.dispatch('refundItem', this.refundItem)
    } else {
      text = "You canceled!";
    }
    document.getElementById("demo").innerHTML = text;
  }
}

}
</script>
 
<style scoped>

.form-container {
  width: 80%;
  margin: 30px auto;
}
       

</style>