odoo.define('exam.email_validation', function (require) {
    'use strict';

    var basic_fields = require('web.basic_fields');
    var field_registry = require('web.field_registry');
    var FieldEmail = basic_fields.FieldEmail;
    var core = require('web.core');
    var _t = core._t;

    var EmailValidation = FieldEmail.include({
        events: _.extend({},FieldEmail.prototype.events,{
            'blur': '_onKeyUp',
        }),
        init: function (parent, action) {
            this._super.apply(this, arguments);
        },
        _onKeyUp: function (e) {
            var self = this;
            var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            var validatoin = re.test(String(this.value).toLowerCase())
            if (validatoin == false){
                self.do_warn(_t('Error'),'Please enter valid email!');
                    return false;
            }
        }
    })

});
