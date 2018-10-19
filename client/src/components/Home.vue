<template>
    <div>
        <md-steppers md-alternative md-dynamic-height>
            <md-step id="first" md-label="Insurance">
                <div>
                    <p>Insurance plan</p>
                    <md-field>
                        <md-select v-model="input.insurance">
                            <md-option v-for="(plan,index) in plans" :value="plan" :key="index">
                                {{plan}}
                            </md-option>
                        </md-select>
                    </md-field>
                </div>

                <div v-if="otherQuestions">
                    <p>Out of pocket expenses</p>
                    <md-field>
                        <span class="md-prefix">$</span>
                        <md-input v-model="input.outOfPocket"></md-input>
                    </md-field>
                    <p>Copay</p>
                    <md-field>
                        <span class="md-prefix">$</span>
                        <md-input v-model="input.copay"></md-input>
                    </md-field>
                </div>

                <!--<md-button class="md-raised md-primary" @click="cont('first','second')">Continue</md-button>-->
            </md-step>
            <md-step id="second" md-label="Diagnosis">
                <div>
                    <p>Diagnosis</p>
                    <md-field>
                        <md-select v-model="input.diagnosis">
                            <md-option v-for="(diagnosis,index) in diagnosis" :value="diagnosis" :key="index">
                                {{diagnosis}}
                            </md-option>
                        </md-select>
                    </md-field>
                </div>
            </md-step>
            <md-step id="third" md-label="Medications">
                <div>
                    <md-checkbox v-for="(med,index) in medications" v-model="input.medications" :value="med" :key="index" class="md-primary">
                        {{med}}
                    </md-checkbox>
                    <md-button class="md-raised md-primary" @click="calculate()">Calculate</md-button>
                </div>
            </md-step>
            <md-step id="fourth" md-label="Cost">
                Process Complete. Timeline Page is now Viewable
            </md-step>
        </md-steppers>
        
    </div>
    
</template>

<script>
import axios from 'axios';

export default {
    name: 'Home',

    data: () => ({
        plans: ['Duke Select', 'Duke Basic', 'Blue Care', 'Duke Options', 'Other'],
        diagnosis: ['Prostate cancer', 'Lung cancer'],
        medications: ['Medication A', 'Medication B', 'Medication C'],
        input: {
            insurance: null,
            outOfPocket: null,
            copay: null,
            diagnosis: null,
            medications: []
        },
        questions: {
            insurance: false,
            diagnosis: false,
            medications: false
        },
        totalCost: null,
        loading: true
    }),

    computed: {
        otherQuestions() {
            return this.input.insurance==='Other';
        }
    },

    methods: {
        cont(curr, next) {

        },

        calculate() {
            this.loading = true;
            // will want to change path based on whether in prod or dev
            const path = 'http://localhost:5000/calculate';
            axios.post(path, this.input).then((res) => {
                this.loading = false;
                this.totalCost = res.data.cost;
                console.log(this.totalCost);
            }).catch((error) => {
                console.log(error)
            });
        }
    }
}
</script>
