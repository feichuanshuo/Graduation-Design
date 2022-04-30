import React, {Component} from 'react';
import {Route, Routes ,Navigate} from "react-router-dom";
import {Button, Layout} from 'antd';
import {
    MenuUnfoldOutlined,
    MenuFoldOutlined,
} from '@ant-design/icons';
import LeftMenu from "./components/left_menu";
import Header from "./components/header";
import Home from "./components/content/home";
import SupplyData from "./components/content/supply_data";
import TransactionData from "./components/content/transaction_data";
import CityInformation from "./components/content/city_information";
import PublicSentiment from "./components/content/public_sentiment";
import DetailData from "./components/content/detail_data";
import './App.less';

const { Footer, Sider, Content } = Layout;


class App extends Component {
    state = {
        collapsed: true,
    }

    toggle = () => {
        this.setState({
            collapsed: !this.state.collapsed,
        });
    };

    render() {
        const {collapsed} = this.state
        return (
            <Layout className="app">
                <Sider trigger={null} collapsible collapsed={this.state.collapsed}/>
                <Sider className="app-sider" trigger={null} collapsible collapsed={this.state.collapsed}>
                    <LeftMenu/>
                    <Button
                        className="sider-button"
                        block
                        onClick={this.toggle}
                    >
                        <div className="sider-button-icon">
                            {
                                collapsed?<MenuUnfoldOutlined/>:<MenuFoldOutlined/>
                            }
                        </div>
                    </Button>
                </Sider>
                <Layout className="app-layout">
                    <Header/>
                    <Content className="app-layout-content">
                        <Routes>
                            <Route path={"/home"} element={<Home/>}/>
                            <Route path={"/land_information/supply_data"} element={<SupplyData/>}/>
                            <Route path={"/land_information/transaction_data"} element={<TransactionData/>}/>
                            <Route path={"/city_information"} element={<CityInformation/>}/>
                            <Route path={"/public_sentiment"} element={<PublicSentiment/>}/>
                            <Route path={"/detail_data"} element={<DetailData/>}/>
                            <Route path="*" element={<Navigate to="/home"/>} />
                        </Routes>
                    </Content>
                    <Footer className="app-footer">西安房地产发展影响因素分析</Footer>
                </Layout>
            </Layout>
        );
    }
}

export default App;
