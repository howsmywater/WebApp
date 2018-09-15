/**
 * Model describing the water details of a location
 */
export default class WQResult {
    /**
     * @param {Object} opts
     * @param {number} opts.id
     */
    constructor({ id } = {}) {
        this.id = id;
    }
}
