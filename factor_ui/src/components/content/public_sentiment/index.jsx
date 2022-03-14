import React, {Component} from 'react';
import {Card,Input,Row,Col,Tag} from "antd";
import "./index.less";
import axios from "axios";

const { Search } = Input;

class PublicSentiment extends Component {

    baiduSearch = (value) => {
        console.log(value);
        axios.get(`https://index.baidu.com/api/SugApi/sug?inputword[]=${value}&ischeckType=15`).then(res => {
            console.log(res);
        })
    }

    render() {
        return (
            <div>
                <Card
                    className="data-card"
                    title="360指数"
                >
                    <Row
                        className="search-block"
                        gutter={10}
                    >
                        <Col span={8}>
                            <Search
                                placeholder="输入关键词探索以下吧！"
                                enterButton
                                onSearch={this.baiduSearch}
                            />
                            <Tag color="blue">限购</Tag>
                            <Tag color="magenta">土地供应</Tag>
                            <Tag color="green">房地产税</Tag>
                        </Col>
                    </Row>
                </Card>
            </div>
        );
    }
}

export default PublicSentiment;
