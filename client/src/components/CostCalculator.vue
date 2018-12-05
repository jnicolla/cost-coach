<template>
<div>
  <v-content>
    <v-container fluid>

      <v-fab-transition>
        <v-btn
          fab
          absolute bottom right
          v-show="showScrollFab"
          class="mb-5"
          color="#d65f36"
          dark
          @click="$vuetify.goTo(0, {duration: 300,offset: 0,easing: 'easeInOutCubic'})"
        >
        <v-icon dark>arrow_upward</v-icon>
        </v-btn>
      </v-fab-transition>

      <v-layout justify-center row fill-height class="mb-4">
        <v-flex xs11 md8 lg6>
          <v-card>
            <v-container>
              <v-layout>
                <v-flex>
                  <div class="mx-4">
                    <h3 class="display-3 pb-2 font-weight-thin">Cost Calculator</h3>
                    <p>
                      <span class="subheading">The survey below will ask you about your insurance plan, diagnosis, and medications. Once submitted, it will generate a timeline showing you each step you'll take in your cancer treatment until you reach your out-of-pocket maximum.</span>
                    </p>
                    <p>
                      <span class="subheading">Press the "?" button for more details on each part of the survey.</span>
                    </p>
                  </div>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card>
        </v-flex>
      </v-layout>

      <v-layout justify-center row fill-height>
        <v-flex xs11 md8 lg6>
          <v-stepper v-model="stepNo">
            
            <v-stepper-header>
              <template v-for="(step,index) in steps">
                <v-stepper-step
                  :edit-icon="'check'"
                  :complete-icon="getIcon(index)"
                  :step="index + 1"
                  :complete="(index+1)<=stepNo"
                  :editable="(index+1)<stepNo"
                  :key="step"
                  color="#d65f36"
                >
                  {{step}}
                </v-stepper-step>
                <v-divider :key="index" v-if="index<3"></v-divider>
              </template>
            </v-stepper-header>



            <v-stepper-items>
              
              <v-stepper-content step="1" height="400px">
                <v-fab-transition>
                  <v-btn fab small absolute right color="#888" flat 
                    @click="helpDialog=!helpDialog"
                    v-show="!helpDialog"
                  >
                    <v-icon large>help_outline</v-icon>
                  </v-btn>
                </v-fab-transition>
                <h4 class="display-1 font-weight-light grey--text text--darken-3 mb-3">Insurance</h4>
                <v-select
                  :items="insurancePlans"
                  v-model="input.insurance"
                  label="Insurance plan"
                  hint="Select your insurance plan from the dropdown"
                  persistent-hint
                  class="mb-3"
                  color="#d65f36"
                >
                
                </v-select>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn v-if="input.insurance" color="primary" @click.native="stepNo = 2">Continue</v-btn>
                  <v-btn v-else disabled color="primary" @click.native="stepNo = 2">Continue</v-btn>
                </v-card-actions>
              </v-stepper-content>

              <v-stepper-content step="2">
                <v-fab-transition>
                  <v-btn fab small absolute right color="#888" flat 
                    @click="helpDialog=!helpDialog"
                    v-show="!helpDialog"
                  >
                    <v-icon large>help_outline</v-icon>
                  </v-btn>
                </v-fab-transition>
                <h4 class="display-1 font-weight-light grey--text text--darken-3 mb-3">Diagnosis</h4>
                <v-select
                  :items="diagnoses"
                  v-model="input.diagnosis"
                  label="Diagnosis"
                  hint="Select your diagnosis"
                  persistent-hint
                  class="mb-3"
                  color="#d65f36"
                >
                </v-select>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn flat @click.native="stepNo = 1">Back</v-btn>
                  <v-btn v-if="input.diagnosis" color="primary" @click.native="stepNo = 3">Continue</v-btn>
                  <v-btn v-else disabled color="primary" @click.native="stepNo = 3">Continue</v-btn>
                </v-card-actions>
              </v-stepper-content>
              
              <v-stepper-content step="3">
                <v-fab-transition>
                  <v-btn fab small absolute right color="#888" flat 
                    @click="helpDialog=!helpDialog"
                    v-show="!helpDialog"
                  >
                    <v-icon large>help_outline</v-icon>
                  </v-btn>
                </v-fab-transition>
                <h4 class="display-1 font-weight-light grey--text text--darken-3 mb-3">Medications</h4>
                <v-select
                  :items="medications"
                  v-model="input.medications"
                  label="Medications"
                  hint="Select how you take your medications"
                  persistent-hint
                  class="mb-3"
                  color="#d65f36"
                >
                </v-select>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn flat @click.native="stepNo = 2">Back</v-btn>
                  <v-btn v-if="allInputs" color="success" @click.native="submit">Submit</v-btn>
                  <v-btn v-else disabled color="success" @click.native="submit">Submit</v-btn>
                </v-card-actions>
              </v-stepper-content>
              
              <v-stepper-content step="4">
                <transition name="fade" mode="out-in">
                  <div v-if="loading" class="text-xs-center" key="load">
                    <v-progress-circular :size="100" color="#d65f36" indeterminate></v-progress-circular>
                  </div>
                  <div v-else key="tl">
                    <div class="ml-3">
                      <Timeline :data="tlData"></Timeline>
                    </div>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn flat @click.native="resetCalc">Back</v-btn>
                      <v-btn color="primary" outline @click.native="printTimeline">Print</v-btn>
                    </v-card-actions>
                  </div>
                </transition>
              </v-stepper-content>

            </v-stepper-items>
          
          </v-stepper>

          <div class="text-xs-center">
            <v-dialog v-model="helpDialog" max-width="500px">
              <v-card>
                <v-card-title primary-title class="mb-0 pb-0">
                  <h3 class="headline font-weight-light">{{ helpDialogLabel }}</h3>
                </v-card-title>

                <v-card-text>
                  <p class="body-2 font-weight-light grey--text">Fill out each section and press "Continue". Once you have filled out all the steps, you will be taken to a timeline showing each step of your cancer treatment process and when you are expected to reach your out-of-pocket maximum.</p>
                  <p class="title font-weight-regular">{{ helpDialogText }}</p>
                </v-card-text>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <div>
                    <v-btn class="mx-0" color="red" @click="helpDialog=false">
                      <span class="white--text">Close</span>
                    </v-btn>
                  </div>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </div>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</div>
</template>



<script>
import axios from "axios";
import Timeline from './Timeline'

export default {

  data() {
    return {
      /* <div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div> */
      stepNo: 0,

      steps: [
        "Insurance",
        "Diagnosis",
        "Medications",
        "Results"
      ],

      insurancePlans: ["Duke Basic", "Duke Select","Duke Care"],

      diagnoses: ["Prostate Cancer"],

      medications: ["Oral","IV"],

      input: {
        insurance: "",
        diagnosis: "",
        medications: ""
      },

      loading: true,

      tlData: {},

      helpDialogDetails: [
        "This is where you give details that will help the user fill out the insurance section.",
        "Give some information here about how to fill out the diagnosis section should the client open the help dialog.",
        "Do you, the user, need some help filling out the medications section? Here are some more details."
      ],
      helpDialog: false
    }
  },

  components: {
    Timeline
  },

  computed: {
    allInputs() {
      return this.input.insurance && this.input.diagnosis && this.input.medications.length;
    },

    helpDialogLabel() {
      return this.steps[this.stepNo-1];
    },

    helpDialogText() {
      return this.helpDialogDetails[this.stepNo-1];
    },

    showScrollFab() {
      return this.stepNo==4;
    }
  },

  methods: {
    submit() {
      this.stepNo = 4;
      this.loading = true;
      const path = (process.env.NODE_ENV == "production")?
        "https://costcoachserver.herokuapp.com/calculate":"http://localhost:5000/calculate";
      
      axios.post(path, this.input).then((res) => {
        this.tlData = res.data;
        this.loading = false;
      }).catch((err) => {
        console.log(err);
      });
    },

    printTimeline() {
      window.print();
    },

    resetCalc() {
      this.stepNo = 1;
      this.loading = true;
    },

    getIcon(index) {
      return (index<3)? "edit":"assignment";
    }
  }
}
</script>

<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
