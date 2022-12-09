<template lang="">
    <div class="container">
      <div class="banner image-banner">
        <div class="banner-container">
          <div class="banner-section1">
            <h1>Purchase Item</h1>
          </div>
        </div>
      </div>
      <div class="content">
        <div class="items-container">
          <div class="info-container">
            <div class="info-content">
              <h1 class="">Product Info</h1><br/>
              <!-- <h2> Product Name: {{aitemname}}</h2><br><br/> -->
              <img src="../assets/taperecorder.jpg" style="width:200px; left:300px"/>
              <h2 style="top:-35px;right:45px"> Product Name: Taperecorder</h2><br/>
              <h2 style="top:15px;right:400px"> Price: $20 {{aitemprice}}</h2><br>
              <h2 style="top:20px;right:61px" > Brand: Sony{{aitembrand}}</h2><br>
              <!-- <h2 > Brand: {{aitembrand}}</h2><br></br> -->
              <h2 style="top:20px;right:39px"> Location: Bloomington{{aitemlocation}}</h2><br>
            </div>
          </div>
        </div>
        <div class="payment">
        <stripe-checkout
        ref="checkoutRef"
        mode="payment"
        :pk="publishableKey"
        :line-items="lineItems"
        :success-url="successURL"
        :cancel-url="cancelURL"
        @loading="v =>loading = v"
        />
        
              <button style=" position: center; margin-top: 3cm;margin-left:10cm;right:850px; top:120px" type="submit" class="" id="payment_button" @click="submit">
                Purchase
              </button>
              
            </div>
            
        
        <!-- <div class="image-container">
          <h1>PLACEHOLDER Image</h1>
        </div> -->

      </div>
    </div>
  </template>
  <script>
  import Recommendation from '@/components/Recommendation.vue'
  import {StripeCheckout} from '@vue-stripe/vue-stripe'
  export default {
    props: ["aitemimage", "aitemname", "aitemtype", "aitembrand", "aitemlocation", "aitemprice"],
    data(){
      this.publishableKey="pk_test_51M7SfBKnP1V49iZXCX37ZBvX84DbatoQDyETEarDIQPgci4cnhxPmCLgId4w1zeYWkekCDiioYFaAPSRT94LSoAJ00V5Bdi3PD"
          return{
              loading:false,
              lineItems:[
                  {
                      price:'price_1M7SkoKnP1V49iZX2Thvv0Q3',
                      quantity:1
                  }
              ],
              successURL:'http://127.0.0.1:5173/success',
              cancelURL:'http://localhost:8080/error'
  
          }
    },
    
  components:{
          StripeCheckout
      },
      // data(){
      //     this.publishableKey="pk_test_51M7SfBKnP1V49iZXCX37ZBvX84DbatoQDyETEarDIQPgci4cnhxPmCLgId4w1zeYWkekCDiioYFaAPSRT94LSoAJ00V5Bdi3PD"
      //     return{
      //         loading:false,
      //         lineItems:[
      //             {
      //                 price:'price_1M7SkoKnP1V49iZX2Thvv0Q3',
      //                 quantity:1
      //             }
      //         ],
      //         successURL:'http://127.0.0.1:5173/success',
      //         cancelURL:'http://localhost:8080/error'
  
      //     }
      // },
      methods:{
          submit(){
              this.$refs.checkoutRef.redirectToCheckout()
          },
          routeToConfirmation() {
      this.$router.push('/confirmation')
    }
      }
  }
 
  
  
  
  </script>
  <style>
  /* Banner */
  .image-banner {
    /*Photo by <a href="https://unsplash.com/@ollipexxer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Oliver Pecker</a> on <a href="https://unsplash.com/s/photos/technology?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>*/
    background-image: url(../assets/browse-banner.jpg);
    background-position: center center;
  }
  
  .image-banner h1 {
    color: var(--color-highlight);
    font-size: 40px;
  }
  
  .image-banner h2 {
    color: var(--color-highlight);
  }
  
  .banner-section1 {
    width: 100%;
    margin-bottom: 3em;
  }
  
  /* Content */
  .content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin: 0 auto;
    padding: 0;
  }
  
  .items-container {
    width: 45%;
  }
  
  .image-container {
  width: 100%;
  border: 1px solid black;
  margin: 0;
  padding: 0;
  background-image: url(@/assets/Mapbox-Google-Maps-API-Alternative-1024x518.png);
  background-position: top center;
  background-repeat: no-repeat;
}
  
  
  /* Devices */
  /* Devices container */
  
  .info-item-container {
    /* position: relative; */
    margin: 0 15px 30px 0;
  }
  
  .info-content {
    width: 100%;
    display: flex;
    align-items: center;
    flex-flow: row wrap;
  }

  .info-container {
    width: 150%;
    left: 35px;
    border: 1px solid var(--color-primary);
    padding: 4rem 4rem;
    margin: 30px auto;
    border-radius: 5px;
    background-color: var(--color-highlight);
  }
  
  .info-item-container {
    /* position: relative; */
    margin: 0 15px 30px 0;
  }
  
  .paymentinfo-content {
    width: 100%;
    display: flex;
    align-items: center;
    flex-flow: row wrap;
  }
  .paymentinfo-container {
    width: 150%;
    right: 90%;
    top: 300px;
    border: 1px solid var(--color-primary);
    padding: 4rem 4rem;
    margin: 30px auto;
    border-radius: 5px;
    background-color: var(--color-highlight);
    display:flex;
  }
  .my-icon {
    width: 30px;
    height: 30px;
  }
  .search-bar {
    background: transparent;
    outline: none;
    font-size: 20px;
    all: unset;
    width: 100%;
    height: 100%;
    padding: 10px;
  }
  .search-button {
    border: 0;
    border-radius: 50%;
    cursor: pointer;
    background: transparent;
    margin-right: 10px;
  }
  </style>
  