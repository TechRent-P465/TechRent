// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
//import { getAnalytics } from "firebase/analytics";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAub5lAwR32THl2d4MR0IsvIPL2NTOz-tA",
  authDomain: "techrent.firebaseapp.com",
  projectId: "techrent",
  storageBucket: "techrent.appspot.com",
  messagingSenderId: "472978059482",
  appId: "1:472978059482:web:f72c5b421d0969abb575e3",
  measurementId: "G-G5J9ZJS92S",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
//const analytics = getAnalytics(app);
const auth = getAuth();

export { app, auth };
