pragma solidity ^0.8.0;

// SPDX-License-Identifier: MIT

import "../interfaces/IMerkleStash.sol";

contract VotiumZap {

    struct claimParam {
        address distributor;
        uint256 index;
        uint256 amount;
        bytes32[] merkleProof;
    }

    /// @notice Claims all specified rewards in one go
    /// @param claimParams - an array containing the info necessary to claim for
    /// each available token
    function batchClaim(claimParam[] calldata claimParams) external {
        for (uint i = 0; i < claimParams.length; i++) {
            claimParam calldata currentClaim = claimParams[i];
            IMerkleStash distributor = IMerkleStash(currentClaim.distributor);
            distributor.claim(currentClaim.index,
            msg.sender,
            currentClaim.amount,
            currentClaim.merkleProof);
        }
    }

}
