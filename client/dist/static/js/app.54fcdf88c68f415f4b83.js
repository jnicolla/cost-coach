webpackJsonp([1],{"7zck":function(t,e){},FgVN:function(t,e,n){t.exports=n.p+"static/img/WTC4.07d22a9.png"},NHnr:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var s=n("7+uW"),i={render:function(){var t=this.$createElement,e=this._self._c||t;return e("v-footer",{staticClass:"pa-3"},[e("v-spacer"),this._v(" "),e("div",[this._v("CostCoach © "+this._s((new Date).getFullYear()))])],1)},staticRenderFns:[]},a={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-toolbar",{attrs:{color:"#d65f36",dark:""}},[n("v-toolbar-title",[t._v("CostCoach")]),t._v(" "),n("v-spacer"),t._v(" "),n("div",{staticClass:"hidden-sm-and-down"},[n("router-link",{attrs:{to:"/Home"}},[n("v-btn",{attrs:{flat:""}},[t._v("Home")])],1),t._v(" "),n("router-link",{attrs:{to:"/CostCalculator"}},[n("v-btn",{attrs:{flat:""}},[t._v("Cost Calculator")])],1),t._v(" "),n("router-link",{attrs:{to:"/Guide"}},[n("v-btn",{attrs:{flat:""}},[t._v("Conversation Guideline")])],1),t._v(" "),n("router-link",{attrs:{to:"/Disclaimer"}},[n("v-btn",{attrs:{flat:""}},[t._v("Disclaimer")])],1)],1)],1)},staticRenderFns:[]},r={name:"App",components:{Footer:n("VU/8")(null,i,!1,null,null,null).exports,Navbar:n("VU/8")(null,a,!1,null,null,null).exports}},o={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{attrs:{id:"app"}},[e("Navbar"),this._v(" "),e("router-view"),this._v(" "),e("Footer")],1)},staticRenderFns:[]};var c=n("VU/8")(r,o,!1,function(t){n("XMvs")},null,null).exports,l=n("/ocq"),u=n("rJKp"),v=n.n(u),p=n("VpNU"),d=n.n(p),m=n("yAjn"),h=n.n(m),f=n("FgVN"),_=n.n(f),k={data:function(){return{items:[{src:v.a},{src:d.a},{src:h.a},{src:_.a}]}}},b={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("v-carousel",t._l(t.items,function(t,e){return n("v-carousel-item",{key:e,attrs:{src:t.src}})})),t._v(" "),n("v-carousel",{staticStyle:{height:"100%"}},t._l(t.slides,function(e,s){return n("v-carousel-item",{key:s,attrs:{src:e.src}},[n("v-jumbotron",{attrs:{dark:""}},[n("v-container",{attrs:{"fill-height":""}},[n("v-layout",{attrs:{"align-center":""}},[n("v-flex",[n("h3",{staticClass:"display-3"},[t._v(t._s(e.title))]),t._v(" "),n("span",{staticClass:"subheading"},[t._v(t._s(e.text))])])],1)],1)],1)],1)}))],1)},staticRenderFns:[]},g=n("VU/8")(k,b,!1,null,null,null).exports,y=n("mtWM"),x=n.n(y),C={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("h1",[t._v("Your Road to Recovery")]),t._v(" "),n("v-timeline",t._l(t.events,function(e,s){return n("v-timeline-item",{key:e.id,attrs:{color:"primary",large:""}},[n("span",{attrs:{slot:"opposite"},slot:"opposite"},[t._v(t._s(e.date))]),t._v(" "),n("v-card",{staticClass:"elevation-2"},[n("v-card-title",{staticClass:"headline",attrs:{"primary-title":""}},[t._v(t._s(e.visit))]),t._v(" "),s==t.events.length?n("v-card-text",[t._v(" At this stage, you have reached your out-of-pocket maximum")]):n("v-card-text",[t._v("You will be approximately "+t._s(e.money)+" away from reaching your out-of-pocket maximum.")])],1)],1)}))],1)},staticRenderFns:[]},N={data:function(){return{stepNo:0,steps:[{label:"Insurance"},{label:"Diagnosis"},{label:"Medications"}],insurancePlans:["Duke Basic","Duke Select","Duke Care","Duke Option"],diagnoses:["Prostate Cancer"],medications:["Abiraterone","Docetaxel"],input:{insurance:"",diagnosis:"",medications:[]},loading:!0,tlData:{}}},components:{Timeline:n("VU/8")({name:"Timeline",props:["data"],data:function(){return{events:[]}},created:function(){for(var t=0;t<this.data.events.length;t++){var e=this.data.events[t].split(";"),n=e[0],s=e[1],i=e[2];this.events.push({visit:n,date:s,money:i})}}},C,!1,null,null,null).exports},computed:{allInputs:function(){return this.input.insurance&&this.input.diagnosis&&this.input.medications.length}},methods:{submit:function(){var t=this;this.stepNo=4,this.loading=!0;var e="https://costcoachserver.herokuapp.com/test";console.log(e),x.a.post(e,this.input).then(function(e){t.tlData=e.data,t.loading=!1}).catch(function(t){console.log(t)})}}},D={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("v-app",[n("v-content",[n("v-container",{attrs:{fluid:""}},[n("v-stepper",{model:{value:t.stepNo,callback:function(e){t.stepNo=e},expression:"stepNo"}},[n("v-stepper-header",[t._l(t.steps,function(e,s){return n("div",{key:s},[n("v-stepper-step",{attrs:{"edit-icon":"check","complete-icon":"edit",step:s+1,complete:s+1<=t.stepNo,editable:s+1<t.stepNo}},[t._v("\r\n                "+t._s(e.label)+"\r\n              ")])],1)}),t._v(" "),n("v-stepper-step",{attrs:{"edit-icon":"assignment","complete-icon":"assignment",step:4}},[t._v("\r\n              Results\r\n            ")])],2),t._v(" "),n("v-stepper-items",[n("v-stepper-content",{attrs:{step:"1",height:"400px"}},[n("v-select",{attrs:{items:t.insurancePlans,label:"Insurance",hint:"Select your insurance plan from the dropdown","persistent-hint":""},model:{value:t.input.insurance,callback:function(e){t.$set(t.input,"insurance",e)},expression:"input.insurance"}}),t._v(" "),n("v-card-actions",[n("v-spacer"),t._v(" "),t.input.insurance?n("v-btn",{attrs:{color:"primary"},nativeOn:{click:function(e){t.stepNo=2}}},[t._v("Continue")]):n("v-btn",{attrs:{disabled:"",color:"primary"},nativeOn:{click:function(e){t.stepNo=2}}},[t._v("Continue")])],1)],1),t._v(" "),n("v-stepper-content",{attrs:{step:"2"}},[n("v-select",{attrs:{items:t.diagnoses,label:"Diagnosis",hint:"Select your diagnosis","persistent-hint":""},model:{value:t.input.diagnosis,callback:function(e){t.$set(t.input,"diagnosis",e)},expression:"input.diagnosis"}}),t._v(" "),n("v-card-actions",[n("v-spacer"),t._v(" "),n("v-btn",{attrs:{flat:""},nativeOn:{click:function(e){t.stepNo=1}}},[t._v("Back")]),t._v(" "),t.input.diagnosis?n("v-btn",{attrs:{color:"primary"},nativeOn:{click:function(e){t.stepNo=3}}},[t._v("Continue")]):n("v-btn",{attrs:{disabled:"",color:"primary"},nativeOn:{click:function(e){t.stepNo=3}}},[t._v("Continue")])],1)],1),t._v(" "),n("v-stepper-content",{attrs:{step:"3"}},[n("v-select",{attrs:{items:t.medications,label:"Medications",hint:"Select your medications","persistent-hint":"",multiple:""},model:{value:t.input.medications,callback:function(e){t.$set(t.input,"medications",e)},expression:"input.medications"}}),t._v(" "),n("v-card-actions",[n("v-spacer"),t._v(" "),n("v-btn",{attrs:{flat:""},nativeOn:{click:function(e){t.stepNo=2}}},[t._v("Back")]),t._v(" "),t.allInputs?n("v-btn",{attrs:{color:"success"},nativeOn:{click:function(e){return t.submit(e)}}},[t._v("Submit")]):n("v-btn",{attrs:{disabled:"",color:"success"},nativeOn:{click:function(e){return t.submit(e)}}},[t._v("Submit")])],1)],1),t._v(" "),n("v-stepper-content",{attrs:{step:"4"}},[n("div",{staticClass:"text-xs-center"},[t.loading?n("v-progress-circular",{attrs:{size:100,color:"primary",indeterminate:""}}):n("div",[n("Timeline",{attrs:{data:t.tlData}})],1)],1)])],1)],1)],1)],1)],1)],1)},staticRenderFns:[]},w=n("VU/8")(N,D,!1,null,null,null).exports,F={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",[e("center",[e("font",{attrs:{color:"white"}},[this._v(".")])],1),this._v(" "),e("center",[e("font",{attrs:{color:"white"}},[this._v(".")])],1),this._v(" "),e("center",[e("font",{attrs:{color:"white"}},[this._v(".")])],1),this._v(" "),e("v-jumbotron",{attrs:{color:"#232859",dark:""}},[e("v-container",{attrs:{"fill-height":""}},[e("v-layout",{attrs:{"align-center":""}},[e("v-flex",{attrs:{"text-xs-center":""}},[e("h3",{staticClass:"display-3"},[this._v("Disclaimer Text goes here")])])],1)],1)],1)],1)},staticRenderFns:[]},V=n("VU/8")(null,F,!1,null,null,null).exports,q=n("l9mu"),$=n.n(q),R={data:function(){return{questions:[{q:"If tomato is a fruit, is ketchup a smoothie?",checked:!1},{q:"If a cyclops closes its eye, is it blinking or winking?",checked:!1},{q:"If you succeed in an attempt to fail, have you succeeded or failed?",checked:!1},{q:"What color does a Smurf turn when you choke it?",checked:!1}]}},computed:{checkedQs:function(){return this.questions.filter(function(t){return t.checked}).map(function(t){return t.q})}},methods:{genPDF:function(){var t=new $.a;t.text(30,30,this.checkedQs),t.save("Questions.pdf")}}},O={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("v-container",{attrs:{fluid:""}},[n("v-layout",{attrs:{row:"",wrap:""}},[n("v-flex",{attrs:{xs12:"",sm4:"",md4:""}},t._l(t.questions,function(e){return n("v-checkbox",{key:e.id,attrs:{label:e.q,value:e.q,color:"red","hide-details":""},model:{value:e.checked,callback:function(n){t.$set(e,"checked",n)},expression:"question.checked"}})}))],1)],1),t._v(" "),n("v-btn",{attrs:{round:"",color:"#d65f36",dark:""},on:{click:t.genPDF}},[t._v("Create PDF")])],1)},staticRenderFns:[]},U=n("VU/8")(R,O,!1,null,null,null).exports;s.default.use(l.a);var E=new l.a({routes:[{path:"/",name:"Home",component:g},{path:"/Home",name:"Home",component:g},{path:"/CostCalculator",name:"CostCalculator",component:w},{path:"/Disclaimer",name:"Disclaimer",component:V},{path:"/Guide",name:"Guide",component:U}]}),T=n("3EgV"),S=n.n(T);n("7zck");s.default.use(S.a),s.default.config.productionTip=!1,new s.default({el:"#app",router:E,components:{App:c},template:"<App/>"})},VpNU:function(t,e,n){t.exports=n.p+"static/img/WTC2.db7761b.png"},XMvs:function(t,e){},rJKp:function(t,e,n){t.exports=n.p+"static/img/WTC1.b1b96aa.png"},yAjn:function(t,e,n){t.exports=n.p+"static/img/WTC3_v1.24d27de.png"}},["NHnr"]);
//# sourceMappingURL=app.54fcdf88c68f415f4b83.js.map