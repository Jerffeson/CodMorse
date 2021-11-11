import React,  {useState, useEffect} from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import { ToastContainer, toast } from 'react-toastify';
import axios from "axios";
import './styles.css';

const MorseToText = (props) => {
    const [text, setText] = useState("");
    return (
        <div>
            <Formik
                enableReinitialize 
                initialValues={{cod_morse:""}}
                validate={values => {
                    const errors = {};
                    if (!values.cod_morse) {
                        errors.nome = 'Código Morse é obrigatório!';
                    }
                    return errors;
                }}
                onSubmit={ async (values, {resetForm}) => {                
                                       
                    let param = {
                        codMorseParam: values.cod_morse
                    };
                    
                    const api = axios.create({
                        baseURL: "http://localhost",
                        responseType: "json"
                      });
                      
                    await api.get('/api/morse', param)
                    .then(function (response) {
                        setText(text+response.data.data);                                                 
                    });                                             
                                        
                }}
                >
                {({ isSubmitting }) => (
                    <Form className="form-padrao">
                        <label htmlFor="cod_morse">Código Morse</label>
                        <Field type="text" name="cod_morse" placeholder=". ou -"/>
                        <ErrorMessage name="cod_morse" component="div" className="error-message"/>
     
                        <div className="submit-box">                            
                            <div>
                                <button type="submit">
                                    Converter
                                </button> 
                            </div>                         
                        </div>
                    </Form>
                )}
                </Formik>
                <ToastContainer />
                <h1>{text}</h1>
        </div>
    );
}

export default MorseToText;