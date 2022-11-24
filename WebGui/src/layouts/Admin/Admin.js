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
import React from "react";
import {
  Route,
  Switch,
  Redirect,
  useLocation,
  browserHistory,
} from "react-router-dom";
// javascript plugin used to create scrollbars on windows

// core components
import AdminNavbar from "components/Navbars/AdminNavbar.js";
import Footer from "components/Footer/Footer.js";
import Sidebar from "components/Sidebar/Sidebar.js";
import FixedPlugin from "components/FixedPlugin/FixedPlugin.js";

import routes from "routes.js";

import logo from "assets/img/SEL-Logo.png";
import { BackgroundColorContext } from "contexts/BackgroundColorContext";
import PerfectScrollbar from "react-perfect-scrollbar";
import "react-perfect-scrollbar/dist/css/styles.css";
var ps;

function Admin(props) {
  const location = useLocation();
  const mainPanelRef = React.useRef(null);
  const [sidebarOpened, setsidebarOpened] = React.useState(
    document.documentElement.className.indexOf("nav-open") !== -1
  );
  // React.useEffect(() => {
  //   if (navigator.platform.indexOf("Win") > -1) {
  //     document.documentElement.className += " perfect-scrollbar-on";
  //     document.documentElement.classList.remove("perfect-scrollbar-off");
  //     ps = new PerfectScrollbar(mainPanelRef.current, {
  //       suppressScrollX: true
  //     });
  //     let tables = document.querySelectorAll(".table-responsive");
  //     for (let i = 0; i < tables.length; i++) {
  //       ps = new PerfectScrollbar(tables[i]);
  //     }
  //   }
  //   // Specify how to clean up after this effect:
  //   return function cleanup() {
  //     if (navigator.platform.indexOf("Win") > -1) {
  //       ps.destroy();
  //       document.documentElement.classList.add("perfect-scrollbar-off");
  //       document.documentElement.classList.remove("perfect-scrollbar-on");
  //     }
  //   };
  // });
  // React.useEffect(() => {
  //   if (navigator.platform.indexOf("Win") > -1) {
  //     let tables = document.querySelectorAll(".table-responsive");
  //     for (let i = 0; i < tables.length; i++) {
  //       ps = new PerfectScrollbar(tables[i]);
  //     }
  //   }
  //   document.documentElement.scrollTop = 0;
  //   document.scrollingElement.scrollTop = 0;
  //   if (mainPanelRef.current) {
  //     mainPanelRef.current.scrollTop = 0;
  //   }
  //   ps.update()
  // }, [location]);
  // this function opens and closes the sidebar on small devices
  const toggleSidebar = () => {
    document.documentElement.classList.toggle("nav-open");
    setsidebarOpened(!sidebarOpened);
  };
  const getRoutes = (routes) => {
    return routes.map((prop, key) => {
      if (prop.layout === "/admin") {
        return (
          <Route
            path={prop.layout + prop.path}
            component={prop.component}
            key={key}
          />
        );
      } else {
        return null;
      }
    });
  };
  const getBrandText = (path) => {
    for (let i = 0; i < routes.length; i++) {
      if (location.pathname.indexOf(routes[i].layout + routes[i].path) !== -1) {
        return routes[i].name;
      }
    }
    return "Brand";
  };
  return (
    <BackgroundColorContext.Consumer>
      {({ color, changeColor }) => (
        <React.Fragment>
          <div className="wrapper">
            <div
              className="main-panel container-fluid"
              ref={mainPanelRef}
              data={color}
            >
              <div className="row">
                <div className="col-12">
                  <AdminNavbar
                    brandText={getBrandText(location.pathname)}
                    toggleSidebar={toggleSidebar}
                    sidebarOpened={sidebarOpened}
                  />
                </div>
              </div>
              <div className="row mb-3">
                <div className="col-auto">
                  <Sidebar
                    routes={routes}
                    logo={{
                      text: "Fault Signal Generator",
                      // imgSrc: logo
                    }}
                    toggleSidebar={toggleSidebar}
                  />
                </div>
                <div className="col flex-column mb-3">
                  <div className="row-fluid">
                    <Switch>
                      {getRoutes(routes)}
                      <Redirect from="*" to="/admin/dashboard" />

                    </Switch>
                  </div>


                </div>
                {
                          // we don't want the Footer to be rendered on map page
                          location.pathname === "/admin/maps" ? null : (
                            <Footer fluid />
                          )
                        }
              </div>

            </div>

          </div>
        </React.Fragment>
      )}
    </BackgroundColorContext.Consumer>
  );
}

export default Admin;
