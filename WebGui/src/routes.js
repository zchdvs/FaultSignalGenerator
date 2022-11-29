/*!

=========================================================
* Black Dashboard React v1.2.1
=========================================================

* Product Page: https://www.creative-tim.com/product/black-dashboard-react
* Copyright 2022 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/black-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import COMTRADE from "views/COMTRADE.js";
import SignalCreation from "views/SignalCreation.js";
import Documentation from "views/Documentation.js";


var routes = [
  {
    path: "/COMTRADE",
    name: "COMTRADE File",
    icon: "fa-solid fa-file-waveform",
    component: COMTRADE,
    layout: "/admin"
  },
  {
    path: "/SignalCreation",
    name: "Signal Creation",
    icon: "fa-solid fa-wave-square",
    component: SignalCreation,
    layout: "/admin"
  },
  {
    path: "/Documentation",
    name: "Documentation",
    icon: "fa-solid fa-book-atlas",
    component: Documentation,
    layout: "/admin"
  }
];

export default routes;
