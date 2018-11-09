<template>

<div>
      <v-container fluid>
        <v-layout row wrap>
          <v-flex xs12 sm4 md4>
            <v-checkbox v-for="question in questions" :key="question.id"
              :label="question.q"
              :value="question.q"
              color="red"
              hide-details
              v-model="question.checked"
            ></v-checkbox>
          </v-flex>
        </v-layout>
      </v-container>
       <v-btn round color="#d65f36" dark @click="genPDF">Create PDF</v-btn>

</div>       
</template>

<script>
import jsPDF from "jspdf"

export default {
  data() {
    return {
      questions:[
        {
          q:"If tomato is a fruit, is ketchup a smoothie?",
          checked:false
        },
        {q:"If a cyclops closes its eye, is it blinking or winking?", checked:false},
        {q:"If you succeed in an attempt to fail, have you succeeded or failed?", checked:false},
        {q:"What color does a Smurf turn when you choke it?", checked:false}
      ]
    }
  },

  computed: {
    checkedQs() {
      return this.questions.filter((question) => {
        return question.checked;
      }).map((question) => {
        return question.q;
      });
    }
  },

  methods: {
    genPDF() {
      var doc = new jsPDF();
      doc.text(30,30,this.checkedQs);
      doc.save("Questions.pdf");
    }
  }
}
</script>